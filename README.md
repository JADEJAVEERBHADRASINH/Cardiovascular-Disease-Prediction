# 🫀 CardioAI — Cardiovascular Disease Risk Screening Platform

> **AI-Powered Cardiovascular Risk Screening & Clinical Analytics Platform**  
> Semester 5 Machine Learning Project &bull; Department of Computer Engineering, Darshan University  
> **Author:** Veerbhadrasinh &bull; **Academic Year:** 2025–2026 &bull; **Standard Operating Procedure (SOP) Compliant**

---

## Table of Contents
1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [Dataset](#dataset)
4. [Features](#features)
5. [Exploratory Data Analysis (EDA)](#eda)
6. [Feature Engineering](#feature-engineering)
7. [Machine Learning Models](#machine-learning-models)
8. [Random Forest](#random-forest)
9. [AdaBoost (Recommended Model)](#adaboost)
10. [Cross Validation](#cross-validation)
11. [Hyperparameter Tuning](#hyperparameter-tuning)
12. [Scratch Implementation](#scratch-implementation)
13. [Model Evaluation & Benchmarks](#model-evaluation)
14. [Web Application Architecture](#web-application)
15. [Technology Stack](#technology-stack)
16. [Project Structure](#project-structure)
17. [How to Run Locally](#how-to-run-locally)
18. [Deployment Guide](#deployment)
19. [Limitations](#limitations)
20. [Medical Disclaimer](#medical-disclaimer)

---

## 🌟 Overview
**CardioAI** is an end-to-end machine learning system developed to assess cardiovascular disease risk from routine non-invasive clinical indicators. Built using a cohort of **70,000 real-world patient records**, the application guides users and clinical researchers through:
- In-depth Exploratory Data Analysis (EDA)
- Rigorous data preprocessing and feature transformations
- Supervised ensemble machine learning (AdaBoost and Random Forest)
- Mathematical algorithm implementation from scratch without libraries
- A full-featured web dashboard and REST API microservice

---

## 🎯 Problem Statement
Cardiovascular diseases (CVDs) remain the leading cause of mortality globally, taking an estimated 17.9 million lives each year according to the World Health Organization (WHO). Early arterial stiffening and plaque progression often advance asymptomatically. 

The objective of this project is to construct a reproducible supervised machine learning pipeline capable of screening patients early using non-invasive clinical parameters—such as blood pressure, cholesterol categories, fasting glucose, and biometrics—to alert patients and assist triage for specialized diagnostic cardiology.

---

## 📂 Dataset
The dataset utilized is the **Cardiovascular Disease Dataset** (`cardio_train.csv`):
- **Total Records:** 70,000 patient encounters
- **Format:** Semicolon-delimited CSV
- **Missing Values:** Exactly 0 null/NaN entries
- **Duplicate Records:** 0 duplicate rows
- **Target Variable:** `cardio` (Binary classification: `0` for healthy, `1` for diagnosed cardiovascular disease)
- **Target Distribution:** 50.03% healthy (35,021) vs 49.97% diagnosed (34,979) — perfectly balanced, eliminating majority-class bias.

---

## 🧬 Features
The predictive model uses 11 standardized clinical features:

| Feature | Type | Unit / Encoding | Description |
|---|---|---|---|
| `gender` | Categorical | 1: Female, 2: Male | Biological sex at birth |
| `height` | Continuous | cm | Measured patient stature |
| `weight` | Continuous | kg | Measured body weight |
| `ap_hi` | Continuous | mmHg | Systolic blood pressure |
| `ap_lo` | Continuous | mmHg | Diastolic blood pressure |
| `cholesterol` | Categorical | 1: Normal, 2: Above Normal, 3: High | Serum cholesterol level |
| `gluc` | Categorical | 1: Normal, 2: Above Normal, 3: High | Fasting blood glucose level |
| `smoke` | Binary | 0: No, 1: Yes | Active tobacco smoking |
| `alco` | Binary | 0: No, 1: Yes | Regular alcohol consumption |
| `active` | Binary | 0: No, 1: Yes | Routine physical exercise (≥150 min/wk) |
| `age_years` | Continuous | Years | Patient age in solar decimal years |

---

## 📊 EDA (Exploratory Data Analysis)
The project includes meaningful, responsive visualizations exploring multi-variable correlations:
1. **Target Distribution:** Verifies an exact ~50/50 balance between healthy and diseased classes.
2. **Age Distribution:** Demonstrates that cardiovascular disease incidence increases significantly beyond 53–55 years.
3. **Gender Breakdown:** Shows that while females represent ~65% of recorded encounters, disease rates remain comparable (~50%) across sexes.
4. **Hemodynamic Blood Pressure:** Shows strong clustering of disease cases when systolic blood pressure exceeds 135 mmHg and diastolic exceeds 85 mmHg.
5. **Serum Cholesterol:** Demonstrates that patients with high cholesterol (Tier 3) experience a 76.6% disease incidence compared to 23.5% in the normal cohort.
6. **Fasting Glucose:** Confirms elevated glucose levels correlate with microvascular stress and higher risk.
7. **Body Mass Index (BMI):** Shows an upward median shift in the diseased cohort into overweight and obesity categories.
8. **Physical Activity:** Demonstrates a consistent cardioprotective effect with lower disease prevalence among active patients.
9. **Tobacco & Alcohol:** Visualizes earlier onset of vascular strain in smoking and alcohol-consuming cohorts.
10. **Height vs. Weight:** Displays biometric distribution patterns across healthy and diseased cohorts.

---

## ⚙️ Feature Engineering
1. **Solar Age Standardization:**
   $$\text{age\_years} = \frac{\text{age (days)}}{365.0}$$
   Raw patient age is recorded as integer days (e.g., 19,468 days). Converting to decimal solar years improves interpretability and numerical stability without losing variance.
2. **Body Mass Index (BMI):**
   $$\text{BMI} = \frac{\text{weight (kg)}}{(\text{height (m)})^2}$$
   Used dynamically in the web interface and analytics dashboard to categorize patients into Underweight, Normal, Overweight, and Obesity tiers.
3. **Training / Inference Parity:**
   Identical transformation logic and strictly identical feature ordering (`['gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'age_years']`) are enforced across both offline training and online web inference.

---

## 🧪 Train / Test Split
- **Training Set:** 80% (56,000 records)
- **Holdout Test Set:** 20% (14,000 records)
- **Configuration:** `test_size=0.20`, `random_state=42`, `stratify=y`
- **Academic Rationale:** Stratification ensures identical 50.0% class distribution across training and testing sets, preventing sampling bias. The holdout test set was isolated and untouched during training to prevent data leakage.

---

## 🌲 Random Forest
- **Architecture:** `RandomForestClassifier(n_estimators=100, random_state=42)`
- **Training Score:** 99.98%
- **Test Score:** 71.56%
- **Score Gap:** **28.42 percentage points**
- **Overfitting Analysis:** The substantial gap between training and testing accuracy demonstrates **overfitting**. Because decision trees were unconstrained in depth, individual trees memorized sample noise rather than generalizable clinical patterns.

---

## ⚡ AdaBoost (Recommended Model)
- **Architecture:** `AdaBoostClassifier(n_estimators=100, random_state=42)`
- **Test Accuracy:** **72.46%**
- **Precision:** **76.21%**
- **Recall:** **65.25%**
- **F1-Score:** **70.31%**
- **ROC-AUC:** **79.15%**
- **Selection Rationale:** AdaBoost combines sequential decision stumps (depth=1), iteratively re-weighting previously misclassified records. It achieved superior generalization with a minimal overfitting gap (0.64%), making it the selected production model.

---

## 🔄 Cross Validation
To verify stability, **5-Fold Stratified Cross Validation** was performed on the training data:
- **Fold 1:** 71.44%
- **Fold 2:** 72.08%
- **Fold 3:** 71.30%
- **Fold 4:** 71.40%
- **Fold 5:** 72.17%
- **Average CV Score:** **71.68%**
- **Score Spread:** **0.87 percentage points** (Max: 72.17% &minus; Min: 71.30%)
- **Conclusion:** The low spread of 0.87% confirms high model stability across varying patient training subsets.

---

## 🔧 Hyperparameter Tuning (SOP Phase 9)
Systematic hyperparameter tuning was conducted using `GridSearchCV` on the training partition:
1. **Random Forest Tuning:**
   - Evaluated parameters: `max_depth: [10, 15, 20]`, `min_samples_leaf: [2, 5, 10]`, `n_estimators: [100]`.
   - **Best Parameters:** `max_depth=15`, `min_samples_leaf=5`, `n_estimators=100`.
   - **Tuned Results:** Training Accuracy dropped from 99.98% to **77.76%**, while Test Accuracy rose to **73.21%**.
   - **Overfitting Gap:** Slashed from **28.42%** down to **4.55%**, successfully mitigating the memorization defect.
2. **AdaBoost Tuning:**
   - Evaluated `n_estimators: [50, 100, 150]` and `learning_rate: [0.5, 0.8, 1.0]`.
   - **Best Parameters:** `n_estimators=150`, `learning_rate=1.0`.
   - Test Accuracy: **72.49%**, maintaining robust generalization.

---

## 🎓 Scratch Implementation (SOP Phase 10)
To fulfill the mandatory viva constraint (*"Implementation of at least one algorithm without the use of a library"*), a binary **Logistic Regression** classifier was developed from first principles in `utils/scratch_model.py`:
- **Hypothesis:** $\hat{y} = \sigma(Xw + b) = \frac{1}{1 + e^{-(Xw + b)}}$
- **Loss Function:** Binary Cross-Entropy Loss:
  $$L = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$
- **Optimization:** Batch Gradient Descent with analytical gradients:
  $$\frac{\partial L}{\partial w} = \frac{1}{N} X^T (\hat{y} - y), \quad \frac{\partial L}{\partial b} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i)$$
- **Test Performance:**
  - Accuracy: **65.14%** | Precision: **66.17%** | Recall: **61.85%** | F1: **63.94%**
  - Learned weights: `age_years` (+0.445), `cholesterol` (+0.401), `ap_hi` (+0.395), `active` (&minus;0.069, indicating a protective factor).

---

## 📈 Model Evaluation & Comparison Summary

| Model | Source | Train Score | Test Accuracy | Overfitting Gap | Precision | Recall | F1-Score |
|---|---|---|---|---|---|---|---|
| **Random Forest (Baseline)** | Scikit-Learn | 99.98% | 71.56% | 28.42% | 72.04% | 70.41% | 71.22% |
| **AdaBoost (Baseline & Recommended)** | Scikit-Learn | 73.10% | **72.46%** | 0.64% | **76.21%** | 65.25% | **70.31%** |
| **Random Forest (Tuned)** | Scikit-Learn | 77.76% | **73.21%** | 4.55% | 75.36% | **68.94%** | **72.01%** |
| **AdaBoost (Tuned)** | Scikit-Learn | 73.18% | 72.49% | 0.69% | 76.11% | 65.49% | 70.41% |
| **Logistic Regression (Scratch)** | Pure NumPy | 65.20% | 65.14% | 0.06% | 66.17% | 61.85% | 63.94% |

---

## 💻 Web Application
The user interface is designed as a **Premium Medical AI Dashboard** (`CARDIOAI`):
- **Overview:** Project hero, statistics (70,000 records, 11 features, 2+ models, 72.46% Model Evaluation Accuracy), key capabilities.
- **Risk Prediction:** Multi-section form (Patient Profile, Vitals, Health Indicators), real-time interactive BMI needle gauge, model selector, probability gauge, risk classification ("Low Risk" / "Elevated Risk"), and clinical factor attribution pills.
- **Analytics:** 10 responsive Plotly charts exploring multi-variable correlations.
- **Model Insights:** Visual 9-stage ML pipeline breakdown and viva defense talking points.
- **Evaluation:** Overfitting audit scorecard, cross-validation chart, hyperparameter tuning comparison, scratch algorithm code walkthrough, and metric definitions.
- **Health Guidance:** Educational clinical guidelines across 7 modifiable cardiovascular risk domains.
- **About Project:** Academic metadata, student details, technology stack specifications, and disclaimers.

---

## 🛠️ Technology Stack
- **Programming Language:** Python 3.10+ / 3.13
- **Machine Learning:** Scikit-learn, Joblib, NumPy
- **Data Engineering:** Pandas
- **Interactive Visualization:** Plotly Graph Objects & Express
- **Frontend Dashboard:** Streamlit, HTML5, CSS3
- **REST API Microservice:** FastAPI, Pydantic, Uvicorn

---

## 📁 Project Structure
```
Cardiovascular Disease Project/
│
├── app.py                      # Main Streamlit application entry point & router
├── cardio_train.csv            # 70,000 records cardiovascular dataset
├── MLProj.ipynb                # Preserved & enriched Jupyter notebook with SOP steps
├── train_models.py             # Reproducible training & artifact generation script
├── requirements.txt            # Python package dependencies
├── README.md                   # Comprehensive academic project documentation
├── .gitignore                  # Git ignore rules for clean repository
├── render.yaml                 # Render cloud deployment blueprint
│
├── .streamlit/
│   └── config.toml             # Streamlit server and light medical theme config
│
├── Backend/                    # FastAPI REST API Microservice
│   ├── Dockerfile              # Docker container configuration
│   ├── main.py                 # FastAPI endpoints (/, /health, /predict)
│   ├── schemas.py              # Pydantic input/output validation models
│   └── requirements.txt        # Backend dependencies
│
├── components/                 # Modular Streamlit UI components
│   ├── banners.py              # Clinical result banners & medical disclaimers
│   ├── cards.py                # Stat cards, factor pills, pipeline cards
│   ├── charts.py               # Plotly risk gauge, BMI scale, CV charts
│   ├── navbar.py               # Top navigation bar
│   └── sidebar.py              # Academic sidebar context
│
├── pages_app/                  # Application views
│   ├── overview.py             # Hero & project overview
│   ├── prediction.py           # Clinical prediction form & risk assessment
│   ├── analytics.py            # 10 interactive exploratory data charts
│   ├── insights.py             # Visual ML pipeline architecture
│   ├── evaluation.py           # Benchmarks, overfitting audit, scratch algorithm
│   ├── guidance.py             # Evidence-based cardiovascular lifestyle advice
│   └── about.py                # Academic context & technology specifications
│
├── model/                      # Pre-trained model artifacts & metadata
│   ├── cardio_adaboost.joblib  # Trained production AdaBoost model
│   ├── cardio_rf.joblib        # Trained baseline Random Forest model
│   ├── cardio_rf_tuned.joblib  # Trained tuned Random Forest model
│   ├── cardio_adaboost_tuned.joblib # Trained tuned AdaBoost model
│   ├── feature_columns.json    # Exact feature ordering metadata
│   └── model_metrics.json      # Ground truth metrics & validation scores
│
├── services/                   # Business logic & services
│   ├── data_loader.py          # Cached dataset loader (@st.cache_data)
│   └── predictor.py            # High-speed in-process inference engine
│
└── utils/                      # Utilities & helpers
    ├── constants.py            # Color tokens, thresholds, ground truth metrics
    ├── helpers.py              # BMI calculation, input validation, factor attribution
    └── scratch_model.py        # Pure Python/NumPy Logistic Regression from scratch
```

---

## 🚀 How to Run Locally

### 1. Clone or Open the Repository
```bash
cd "Cardiovascular Disease Project"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify / Retrain Model Artifacts (Optional)
The models and metadata are already pre-trained and saved in `model/`. To re-execute the entire pipeline:
```bash
python train_models.py
```

### 4. Run the Streamlit Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### 5. Run the FastAPI Backend (Optional)
In a separate terminal:
```bash
cd Backend
uvicorn main:app --reload --port 8000
```
Interactive Swagger documentation will be available at `http://127.0.0.1:8000/docs`.

---

## ☁️ Deployment Guide

### Deployment on Streamlit Community Cloud (Recommended Single-URL Demo)
1. Push the repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Click **New app**, select your repository, set the branch to `main`, and main file path to `app.py`.
4. Click **Deploy!**
*The application runs 100% self-contained using cached local model artifacts—no localhost, external servers, or uvicorn commands required.*

### Deployment on Render (FastAPI Docker Microservice)
1. Sign in to [render.com](https://render.com).
2. Connect your GitHub repository.
3. Render detects `render.yaml` and deploys `Backend/Dockerfile`.

---

## ⚠️ Limitations
- **Observational Dataset:** Features represent observational data from cross-sectional clinical visits; predictions reflect statistical association, not verified biological causation.
- **Model Capacity:** Accuracy (~72–73%) reflects the ceiling of routine non-invasive tabular features without invasive cardiac imaging (e.g., coronary angiograms or echocardiograms).
- **Outliers in Hemodynamics:** Raw records contained measurement artifacts (e.g. typographical errors) which were safely bounded for visualization.

---

## ⚖️ Medical Disclaimer
**CardioAI is developed strictly for educational and machine learning demonstration purposes as part of an undergraduate computer engineering curriculum.** 
The predictions generated are based on statistical modeling and **are not a medical diagnosis, clinical prognosis, or substitute for professional medical care**. Always seek the advice of a qualified healthcare provider regarding any cardiovascular symptoms.
