"""
Page: How It Works
Interactive 3-step assessment timeline and full ML pipeline architecture.
"""
import streamlit as st
from components.cards import render_pipeline_card
from components.banners import render_medical_disclaimer

def render():
    st.markdown("""
    <div id="how-it-works" style="padding-top: 10px;"></div>
    <div style="text-align: center; max-width: 800px; margin: 0 auto 36px auto;">
        <div class="ref-hero-pill">
            <span style="color: #20D9C2; font-size: 14px;">⚡</span>
            <span>Workflow & Pipeline</span>
        </div>
        <h2 style="font-size: 40px; font-weight: 800; color: #F8FAFC; margin: 0 0 12px 0; letter-spacing: -1px;">
            How It <span class="text-primary-glow">Works</span>
        </h2>
        <p style="font-size: 16px; color: #94A3B8; margin: 0; line-height: 1.6;">
            Get your heart disease risk assessment in three simple steps, backed by rigorous data science.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 3 Simple Steps Timeline
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("""
        <div class="ref-card" style="text-align: center; height: 100%;">
            <div class="ref-step-circle">
                📋
                <div class="ref-step-badge">01</div>
            </div>
            <div style="font-size: 20px; font-weight: 700; color: #F8FAFC; margin-bottom: 10px;">1. Enter Your Data</div>
            <div style="font-size: 14px; color: #94A3B8; line-height: 1.6;">
                Fill in the standardized clinical form with your physical biometrics, blood pressure readings, cholesterol level, and lifestyle habits.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class="ref-card" style="text-align: center; height: 100%;">
            <div class="ref-step-circle">
                🧠
                <div class="ref-step-badge">02</div>
            </div>
            <div style="font-size: 20px; font-weight: 700; color: #F8FAFC; margin-bottom: 10px;">2. AI Analysis</div>
            <div style="font-size: 14px; color: #94A3B8; line-height: 1.6;">
                Our machine learning model processes your multi-variable feature vector through 100 trained ensemble decision estimators.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown("""
        <div class="ref-card" style="text-align: center; height: 100%;">
            <div class="ref-step-circle">
                📊
                <div class="ref-step-badge">03</div>
            </div>
            <div style="font-size: 20px; font-weight: 700; color: #F8FAFC; margin-bottom: 10px;">3. Get Results</div>
            <div style="font-size: 14px; color: #94A3B8; line-height: 1.6;">
                Receive an instant risk probability score, visual speedometer gauge, key contributing factor tags, and lifestyle recommendations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

    # Technical Viva Pipeline
    st.markdown("""
    <div style="margin-bottom: 18px;">
        <h3 style="font-size: 22px; font-weight: 700; color: #F8FAFC; margin: 0 0 4px 0;">
            🎓 Behind the Scenes: The 7-Stage ML Pipeline
        </h3>
        <div style="font-size: 13px; color: #94A3B8;">
            Architectural stages used to prepare, train, evaluate, and deploy the prediction model.
        </div>
    </div>
    """, unsafe_allow_html=True)

    stages = [
        (1, "Dataset Ingestion", "cardio_train.csv &bull; 70,000 real-world records with 50/50 balanced CVD prevalence."),
        (2, "Data Cleansing", "Verification of 0 missing values, range bounds testing, and type normalization."),
        (3, "Feature Engineering", "Conversion of age days to solar decimal years (age/365) and 11-column feature alignment."),
        (4, "Stratified Split", "80% training (56,000) and 20% holdout test (14,000) with stratify=y."),
        (5, "Model Training", "Benchmarked Random Forest vs AdaBoost (100 estimators each, random_state=42)."),
        (6, "Validation & Overfitting Audit", "5-fold CV (71.68% mean, 0.87% spread) and evaluation of the 28.42% RF overfitting gap."),
        (7, "Dual-Engine Deployment", "Persisted via Joblib with FastAPI backend integration and instant local fallback.")
    ]

    for num, title, desc in stages:
        st.markdown(f"""
        <div style="
            background: #0F172A;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 14px 18px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 16px;
        ">
            <div style="
                width: 32px;
                height: 32px;
                border-radius: 8px;
                background: rgba(20, 184, 166, 0.15);
                color: #20D9C2;
                font-weight: 800;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 14px;
            ">{num}</div>
            <div>
                <span style="font-weight: 700; color: #F8FAFC; font-size: 15px;">{title}:</span>
                <span style="color: #94A3B8; font-size: 13px; margin-left: 6px;">{desc}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    render_medical_disclaimer()
