"""
CardioAI Model Insights Page.
Visual step-by-step breakdown of the Machine Learning Pipeline:
DATASET -> PREPROCESSING -> FEATURE ENGINEERING -> TRAIN/TEST SPLIT -> MODEL TRAINING -> CROSS VALIDATION -> EVALUATION -> PREDICTION.
Includes viva defense cheat-sheet for academic evaluation.
"""
import streamlit as st
from components.cards import render_pipeline_card
from components.banners import render_medical_disclaimer

def render():
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <div class="brand-badge">
            🧠 Machine Learning Pipeline Architecture
        </div>
        <h2 style="font-size: 32px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">
            End-to-End Machine Learning Pipeline
        </h2>
        <p style="font-size: 14px; color: #64748B; margin: 0;">
            Architectural walkthrough of data engineering, model development, validation, and dual-mode inference.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Viva Defense Talking Points Card
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border: 1px solid #BFDBFE;
        border-radius: 16px;
        padding: 22px 26px;
        margin-bottom: 28px;
    ">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
            <span style="font-size: 20px;">🎓</span>
            <div style="font-size: 16px; font-weight: 800; color: #1E40AF;">
                Viva Voce Defense: Key Architectural Decisions
            </div>
        </div>
        <div style="font-size: 13px; color: #1E3A8A; line-height: 1.7;">
            &bull; <b>Why AdaBoost over single Decision Trees?</b> Unconstrained decision trees severely overfit tabular medical data (Random Forest scored 99.98% on training vs 71.56% on test). AdaBoost combines 100 sequential shallow decision stumps, systematically re-weighting hard-to-classify samples to achieve optimal generalization (72.46% test accuracy, 0.56% gap).<br>
            &bull; <b>Why standardize age into decimal years?</b> The raw dataset provides age recorded as integer days (e.g. 19,468 days). Transforming to solar years (<code>age_years = age / 365.0</code>) yields clinical interpretability without loss of variance or precision.<br>
            &bull; <b>How was data leakage prevented?</b> An 80/20 train/test partition was constructed with <code>stratify=y</code> to preserve exactly 50% class balance across both splits, keeping the holdout test set completely untouched during model training.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Step-by-Step Pipeline Flow Cards
    stages = [
        (
            1,
            "DATASET INGESTION",
            "70,000 Patient Examination Records (cardio_train.csv)",
            [
                "Ingested 70,000 anonymized clinical examination records.",
                "Target variable: 'cardio' (binary: 0 = Healthy, 1 = Cardiovascular Disease).",
                "Includes biometric measurements (height, weight), hemodynamics (ap_hi, ap_lo), blood serum chemistry (cholesterol, glucose), and lifestyle habits (smoking, alcohol, activity)."
            ]
        ),
        (
            2,
            "DATA PREPROCESSING & INTEGRITY AUDITING",
            "Missing Value Verification & Plausibility Auditing",
            [
                "Verified zero missing or null (NaN) values across all 70,000 records.",
                "Audited hemodynamic outlier values (recording errors like negative pressures or typographical zeros).",
                "Verified consistent integer and floating-point data types across all clinical features."
            ]
        ),
        (
            3,
            "FEATURE ENGINEERING",
            "Solar Age Normalization & Biometric Transformation",
            [
                "Transformed 'age' from integer days to decimal solar years via formula: <code>age_years = age / 365.0</code>.",
                "Engineered structured 11-dimensional feature vector: <code>['gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'age_years']</code>.",
                "Enforced strictly identical feature transformation logic between offline model training and real-time inference."
            ]
        ),
        (
            4,
            "TRAIN / TEST SPLIT",
            "Stratified 80/20 Holdout Partitioning (seed=42)",
            [
                "Partitioned into 56,000 training records (80%) and 14,000 holdout testing records (20%).",
                "Configured <code>stratify=y</code> to guarantee equal 50.0% class distribution across both partitions.",
                "Fixed <code>random_state=42</code> for strict academic reproducibility."
            ]
        ),
        (
            5,
            "MODEL TRAINING",
            "Ensemble Classifier Implementations (Random Forest & AdaBoost)",
            [
                "Trained baseline RandomForestClassifier (n_estimators=100, random_state=42).",
                "Trained baseline AdaBoostClassifier (n_estimators=100, random_state=42) with decision stumps.",
                "Implemented pure Python & NumPy Scratch Logistic Regression with batch gradient descent."
            ]
        ),
        (
            6,
            "CROSS VALIDATION & STABILITY AUDITING",
            "5-Fold Stratified Cross Validation on Training Data",
            [
                "Audited fold-by-fold consistency across 5 stratified training partitions.",
                "Achieved 71.68% average CV accuracy with a narrow spread of 0.87 percentage points.",
                "Confirmed absence of catastrophic fold collapse or sampling sensitivity."
            ]
        ),
        (
            7,
            "HYPERPARAMETER TUNING",
            "GridSearchCV Regularization on Training Set",
            [
                "Tuned Random Forest constraints (max_depth=15, min_samples_leaf=5, n_estimators=100) to mitigate overfitting.",
                "Reduced Random Forest overfitting gap from 28.42% down to 4.55%, lifting test accuracy to 73.21%.",
                "Tuned AdaBoost estimator configurations (150 estimators, learning_rate=1.0)."
            ]
        ),
        (
            8,
            "MODEL EVALUATION & BENCHMARKING",
            "Holdout Metrics, Confusion Matrices & ROC-AUC",
            [
                "Demonstrated Random Forest memorization (99.98% train vs 71.56% test, gap 28.42%).",
                "Validated AdaBoost superior balance: 72.46% Accuracy, 76.21% Precision, 65.25% Recall, 70.31% F1.",
                "Evaluated Scratch Logistic Regression model achieving 65.14% holdout accuracy."
            ]
        ),
        (
            9,
            "PREDICTION & DEPLOYMENT",
            "Dual-Engine: Standalone In-Process & FastAPI REST Microservice",
            [
                "Persisted trained models to disk via <code>joblib</code> with schema definitions in <code>model/feature_columns.json</code>.",
                "Created responsive Streamlit Web UI with real-time BMI gauge and probability calibration.",
                "Provided FastAPI backend with <code>GET /health</code> and <code>POST /predict</code> for microservice architecture."
            ]
        )
    ]

    for step_num, title, subtitle, bullets in stages:
        render_pipeline_card(step_num, title, subtitle, bullets)

    render_medical_disclaimer()
