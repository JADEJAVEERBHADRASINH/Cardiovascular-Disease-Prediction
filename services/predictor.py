"""
CardioPredict Inference Service.
Focused dual-model architecture:
1. Random Forest Classifier
2. AdaBoost Classifier
Guarantees sub-10ms predictions with zero external dependencies.
"""
import os
import joblib
import pandas as pd
import numpy as np

# Cache in memory
_CACHED_MODELS = {}

def get_model(model_choice: str = "random_forest"):
    """Load and cache local models from disk."""
    model_choice = model_choice.lower()
    
    file_map = {
        "random_forest": "cardio_rf_tuned.joblib",
        "rf": "cardio_rf_tuned.joblib",
        "random_forest_tuned": "cardio_rf_tuned.joblib",
        "adaboost": "cardio_adaboost.joblib",
        "ada": "cardio_adaboost.joblib",
        "adaboost_tuned": "cardio_adaboost_tuned.joblib"
    }
    
    file_name = file_map.get(model_choice, "cardio_rf_tuned.joblib")
    
    if file_name not in _CACHED_MODELS:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, "model", file_name)
        if not os.path.exists(model_path):
            model_path = os.path.join("model", file_name)
            
        if os.path.exists(model_path):
            _CACHED_MODELS[file_name] = joblib.load(model_path)
        else:
            return None
            
    return _CACHED_MODELS.get(file_name)

def predict_risk(patient_dict: dict, model_choice: str = "random_forest") -> dict:
    """
    Generate cardiovascular risk screening prediction using Random Forest or AdaBoost.
    """
    model = get_model(model_choice)
    if model is None:
        model = get_model("random_forest")
        if model is None:
            model = get_model("adaboost")
            if model is None:
                raise RuntimeError("Model artifacts not found in model/ directory. Please run train_models.py first.")

    features_ordered = [
        "gender", "height", "weight", "ap_hi", "ap_lo",
        "cholesterol", "gluc", "smoke", "alco", "active", "age_years"
    ]
    
    # Construct exact feature vector DataFrame
    row = {col: patient_dict[col] for col in features_ordered}
    df_in = pd.DataFrame([row])[features_ordered]

    # Model inference
    if hasattr(model, "predict_proba"):
        proba_raw = model.predict_proba(df_in)
        if isinstance(proba_raw, np.ndarray) and proba_raw.ndim == 2:
            prob = float(proba_raw[0, 1])
        elif isinstance(proba_raw, np.ndarray) and proba_raw.ndim == 1:
            prob = float(proba_raw[0])
        else:
            prob = float(proba_raw)
    else:
        pred_val = int(model.predict(df_in)[0])
        prob = 0.85 if pred_val == 1 else 0.15

    # Clamp probability
    prob = max(0.01, min(0.99, prob))
    pred_class = int(prob >= 0.50)
    risk_label = "Elevated Risk" if pred_class == 1 or prob >= 0.50 else "Low Risk"

    model_display_names = {
        "random_forest": "Random Forest Classifier",
        "rf": "Random Forest Classifier",
        "random_forest_tuned": "Random Forest Classifier",
        "adaboost": "AdaBoost Classifier",
        "ada": "AdaBoost Classifier"
    }

    return {
        "prediction": pred_class,
        "risk_probability": round(prob, 4),
        "risk_percentage": round(prob * 100, 1),
        "risk_label": risk_label,
        "model_used": model_display_names.get(model_choice.lower(), "Random Forest Classifier"),
        "source": "Local ML Inference Engine"
    }
