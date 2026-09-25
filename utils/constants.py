"""
Design tokens, color constants, clinical baseline thresholds, and model benchmark constants.
"""

# Color System - Dark Medical Tech Palette
COLOR_BG_DARK = "#07111F"
COLOR_BG_SURFACE = "#0B1628"
COLOR_PRIMARY_CYAN = "#19C3B1"
COLOR_PRIMARY_GLOW = "#20D9C2"
COLOR_SECONDARY_BLUE = "#4F8CFF"
COLOR_DANGER = "#FF5C6C"
COLOR_WARNING = "#FFB547"
COLOR_SUCCESS = "#10B981"
COLOR_TEXT = "#F5F7FA"
COLOR_MUTED = "#94A3B8"
COLOR_CARD = "rgba(255, 255, 255, 0.04)"
COLOR_BORDER = "rgba(255, 255, 255, 0.08)"

# Feature Ordering (Strictly aligned with model training)
FEATURE_COLUMNS = [
    "gender", "height", "weight", "ap_hi", "ap_lo",
    "cholesterol", "gluc", "smoke", "alco", "active", "age_years"
]

# Ground Truth Metrics from MLProj.ipynb
METRICS_DATA = {
    "records": 70000,
    "features_count": 11,
    "models_count": "2+",
    "eval_accuracy": "72.46%",
    "random_forest": {
        "name": "Random Forest",
        "n_estimators": 100,
        "random_state": 42,
        "train_score": 99.98,
        "test_score": 71.56,
        "score_gap": 28.42,
        "cv_mean": 71.68,
        "cv_spread": 0.87,
        "cv_scores": [71.44, 72.08, 71.30, 71.40, 72.17]
    },
    "adaboost": {
        "name": "AdaBoost",
        "n_estimators": 100,
        "random_state": 42,
        "accuracy": 72.46,
        "precision": 76.21,
        "recall": 65.25,
        "f1": 70.31,
        "roc_auc": 79.15
    }
}

# Clinical Threshold Reference
CLINICAL_THRESHOLDS = {
    "bmi_normal_min": 18.5,
    "bmi_normal_max": 24.9,
    "bmi_overweight_max": 29.9,
    "bp_systolic_normal_max": 120,
    "bp_diastolic_normal_max": 80,
    "bp_systolic_elevated_max": 129,
    "bp_systolic_stage1_max": 139,
    "bp_diastolic_stage1_max": 89
}
