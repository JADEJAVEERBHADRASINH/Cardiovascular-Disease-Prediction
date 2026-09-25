"""
CardioAI Microservice Backend (FastAPI).
Preserves existing root endpoint and adds robust /health and /predict APIs.
Compatible with Linux, macOS, and Windows deployments.
"""
import os
import json
import joblib
import pandas as pd
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from schemas import PatientInput, PredictionOutput, FactorDetail

# Global state for loaded model and metadata
app_state = {
    "model": None,
    "features": [],
    "model_name": "AdaBoost Classifier"
}

def locate_model_file():
    """Locate model file relative to backend directory or project root."""
    backend_dir = Path(__file__).resolve().parent
    project_root = backend_dir.parent
    
    candidates = [
        project_root / "model" / "cardio_adaboost.joblib",
        backend_dir / "model" / "cardio_adaboost.joblib",
        Path("model") / "cardio_adaboost.joblib",
        Path("..") / "model" / "cardio_adaboost.joblib"
    ]
    for p in candidates:
        if p.exists():
            return p
    return None

def locate_features_file():
    """Locate feature columns metadata file."""
    backend_dir = Path(__file__).resolve().parent
    project_root = backend_dir.parent
    
    candidates = [
        project_root / "model" / "feature_columns.json",
        backend_dir / "model" / "feature_columns.json",
        Path("model") / "feature_columns.json",
        Path("..") / "model" / "feature_columns.json"
    ]
    for p in candidates:
        if p.exists():
            return p
    return None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model and feature metadata on startup
    model_path = locate_model_file()
    if model_path and model_path.exists():
        app_state["model"] = joblib.load(str(model_path))
        print(f"[Success] Loaded model: {app_state['model_name']} from {model_path}")
    else:
        print("[Warning] Model file not located during startup. Predictions will attempt on-demand load.")

    feat_path = locate_features_file()
    if feat_path and feat_path.exists():
        with open(feat_path, "r", encoding="utf-8") as f:
            app_state["features"] = json.load(f).get("features", [])

    yield

app = FastAPI(
    title="CardioAI Prediction Microservice",
    description="Machine learning prediction API for cardiovascular disease risk screening.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    """Preserved original health-check route."""
    return {
        "message": "Cardiovascular Disease Prediction API is running"
    }

@app.get("/health")
def health():
    """Detailed system and model health endpoint."""
    return {
        "status": "healthy",
        "model_loaded": app_state["model"] is not None,
        "model_name": app_state["model_name"],
        "features_count": len(app_state["features"]) if app_state["features"] else 11
    }

@app.post("/predict", response_model=PredictionOutput)
def predict(patient: PatientInput):
    """
    Evaluates patient parameters and returns risk probability, class, and factor breakdown.
    """
    model = app_state.get("model")
    if model is None:
        model_path = locate_model_file()
        if model_path and model_path.exists():
            app_state["model"] = joblib.load(str(model_path))
            model = app_state["model"]

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Predictive model artifact is not loaded on server. Run train_models.py first."
        )

    age_years = float(patient.age)

    # Feature vector matching exact trained column sequence
    features_ordered = [
        "gender", "height", "weight", "ap_hi", "ap_lo",
        "cholesterol", "gluc", "smoke", "alco", "active", "age_years"
    ]
    data_dict = {
        "gender": patient.gender,
        "height": patient.height,
        "weight": patient.weight,
        "ap_hi": patient.ap_hi,
        "ap_lo": patient.ap_lo,
        "cholesterol": patient.cholesterol,
        "gluc": patient.gluc,
        "smoke": patient.smoke,
        "alco": patient.alco,
        "active": patient.active,
        "age_years": age_years
    }
    df_in = pd.DataFrame([data_dict])[features_ordered]

    try:
        if hasattr(model, "predict_proba"):
            prob = float(model.predict_proba(df_in)[0, 1])
        else:
            pred_class_raw = int(model.predict(df_in)[0])
            prob = 0.85 if pred_class_raw == 1 else 0.15

        pred_class = int(prob >= 0.50)
        risk_label = "Elevated Risk" if (pred_class == 1 or prob >= 0.50) else "Low Risk"

        # Calculate factor breakdown
        factors = []
        if patient.ap_hi >= 140 or patient.ap_lo >= 90:
            factors.append(FactorDetail(name="Blood Pressure", value=f"{patient.ap_hi}/{patient.ap_lo}", status="Stage 2", impact="High Risk Driver", color="#EF4444"))
        elif patient.ap_hi >= 130 or patient.ap_lo >= 80:
            factors.append(FactorDetail(name="Blood Pressure", value=f"{patient.ap_hi}/{patient.ap_lo}", status="Stage 1", impact="Moderate Impact", color="#F59E0B"))
        else:
            factors.append(FactorDetail(name="Blood Pressure", value=f"{patient.ap_hi}/{patient.ap_lo}", status="Normal", impact="Protective", color="#10B981"))

        bmi = patient.weight / ((patient.height / 100.0) ** 2)
        if bmi >= 30.0:
            factors.append(FactorDetail(name="BMI", value=f"{bmi:.1f}", status="Obese", impact="High Risk Driver", color="#EF4444"))
        elif bmi >= 25.0:
            factors.append(FactorDetail(name="BMI", value=f"{bmi:.1f}", status="Overweight", impact="Elevated Risk", color="#F59E0B"))
        else:
            factors.append(FactorDetail(name="BMI", value=f"{bmi:.1f}", status="Normal", impact="Healthy Baseline", color="#10B981"))

        if patient.cholesterol == 3:
            factors.append(FactorDetail(name="Cholesterol", value="High", status="High", impact="High Risk Driver", color="#EF4444"))
        elif patient.cholesterol == 2:
            factors.append(FactorDetail(name="Cholesterol", value="Above Normal", status="Borderline", impact="Elevated Risk", color="#F59E0B"))
        else:
            factors.append(FactorDetail(name="Cholesterol", value="Normal", status="Normal", impact="Healthy Baseline", color="#10B981"))

        if patient.smoke == 1:
            factors.append(FactorDetail(name="Smoking", value="Active Smoker", status="Active", impact="Vascular Strain", color="#EF4444"))

        return PredictionOutput(
            prediction=pred_class,
            risk_probability=round(prob, 4),
            risk_percentage=round(prob * 100, 1),
            risk_label=risk_label,
            model_used=app_state["model_name"],
            top_contributing_factors=factors
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference error during model execution: {str(e)}"
        )