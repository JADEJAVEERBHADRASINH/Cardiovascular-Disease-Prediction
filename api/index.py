"""
CardioPredict Vercel Serverless API.
Exposes FastAPI endpoints for serverless execution on Vercel (@vercel/python).
Routes:
- GET  /api/health
- POST /api/predict
"""
import os
import json
import joblib
import numpy as np
from pathlib import Path
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="CardioPredict Vercel API",
    description="Cardiovascular Disease Risk Prediction Microservice for Vercel Serverless",
    version="2.0.0"
)

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model cache
MODELS = {}

def get_base_dir() -> Path:
    # Handle both Vercel serverless environment and local dev
    current = Path(__file__).resolve().parent
    if (current.parent / "model").exists():
        return current.parent
    if (current / "model").exists():
        return current
    return Path.cwd()

def load_models():
    base_dir = get_base_dir()
    model_dir = base_dir / "model"
    
    if "adaboost" not in MODELS:
        ada_path = model_dir / "cardio_adaboost.joblib"
        if ada_path.exists():
            MODELS["adaboost"] = joblib.load(str(ada_path))
            
    if "random_forest" not in MODELS:
        rf_path = model_dir / "cardio_rf_tuned.joblib"
        if rf_path.exists():
            MODELS["random_forest"] = joblib.load(str(rf_path))

class PatientRequest(BaseModel):
    age: float = Field(..., ge=1, le=120, description="Age in years")
    gender: int = Field(..., ge=1, le=2, description="1: Female, 2: Male")
    height: float = Field(..., ge=50, le=250, description="Height in cm")
    weight: float = Field(..., ge=20, le=300, description="Weight in kg")
    ap_hi: int = Field(..., ge=60, le=250, description="Systolic Blood Pressure")
    ap_lo: int = Field(..., ge=40, le=200, description="Diastolic Blood Pressure")
    cholesterol: int = Field(..., ge=1, le=3, description="1: Normal, 2: Above Normal, 3: Well Above")
    gluc: int = Field(..., ge=1, le=3, description="1: Normal, 2: Above Normal, 3: Well Above")
    smoke: int = Field(..., ge=0, le=1, description="0: No, 1: Yes")
    alco: int = Field(..., ge=0, le=1, description="0: No, 1: Yes")
    active: int = Field(..., ge=0, le=1, description="0: No, 1: Yes")
    model: str = Field(default="random_forest", description="random_forest or adaboost")

@app.get("/api")
@app.get("/api/health")
def health_check():
    load_models()
    return {
        "status": "online",
        "service": "CardioPredict AI 2.0",
        "models_available": list(MODELS.keys()),
        "academic_context": {
            "institution": "Darshan University",
            "department": "Computer Engineering",
            "student": "Veerbhadrasinh",
            "semester": 5
        }
    }

@app.post("/api/predict")
def predict_cardio(req: PatientRequest):
    load_models()
    model_key = "adaboost" if "ada" in req.model.lower() else "random_forest"
    
    selected_model = MODELS.get(model_key)
    if selected_model is None:
        # Fallback to available model
        selected_model = next(iter(MODELS.values()), None)
        
    if selected_model is None:
        raise HTTPException(status_code=500, detail="Models could not be loaded on serverless worker.")

    # Format vector: ['gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'age_years']
    feature_vector = np.array([[
        req.gender,
        float(req.height),
        float(req.weight),
        int(req.ap_hi),
        int(req.ap_lo),
        int(req.cholesterol),
        int(req.gluc),
        int(req.smoke),
        int(req.alco),
        int(req.active),
        float(req.age)
    ]])

    try:
        proba = float(selected_model.predict_proba(feature_vector)[0][1])
    except Exception as e:
        # If feature names warning occurs, use pandas DataFrame
        import pandas as pd
        cols = ['gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'age_years']
        df_vec = pd.DataFrame(feature_vector, columns=cols)
        proba = float(selected_model.predict_proba(df_vec)[0][1])

    risk_pct = round(proba * 100, 1)
    is_elevated = (proba >= 0.50)
    
    # Calculate BMI and key factors
    height_m = req.height / 100.0
    bmi = round(req.weight / (height_m ** 2), 1)

    factors = []
    if req.ap_hi >= 140 or req.ap_lo >= 90:
        factors.append({"factor": "Hypertension", "impact": "High Risk", "color": "#F43F5E"})
    elif req.ap_hi >= 130:
        factors.append({"factor": "Stage 1 Elevated BP", "impact": "Moderate Risk", "color": "#F59E0B"})
        
    if req.cholesterol > 1:
        factors.append({"factor": "Elevated Cholesterol", "impact": "High Risk", "color": "#F43F5E"})
        
    if bmi >= 30:
        factors.append({"factor": "Obese BMI (≥30)", "impact": "Elevated Risk", "color": "#F43F5E"})
    elif bmi >= 25:
        factors.append({"factor": "Overweight BMI", "impact": "Moderate Risk", "color": "#F59E0B"})
        
    if req.smoke == 1:
        factors.append({"factor": "Tobacco Smoker", "impact": "High Risk", "color": "#F43F5E"})
        
    if req.active == 1:
        factors.append({"factor": "Regular Physical Activity", "impact": "Protective Factor", "color": "#10B981"})

    return {
        "prediction": int(is_elevated),
        "risk_probability": round(proba, 4),
        "risk_percentage": risk_pct,
        "risk_label": "Elevated Cardiovascular Risk" if is_elevated else "Low Cardiovascular Risk",
        "model_used": "AdaBoost Classifier (72.5% Acc)" if model_key == "adaboost" else "Random Forest Tuned (73.1% Acc)",
        "bmi": bmi,
        "contributing_factors": factors
    }
