"""
CardioPredict About Project Page.
Academic documentation, tech stack specifications, dataset context, and viva notes.
Department of Computer Engineering, Darshan University.
Student: Veerbhadrasinh • Semester 5 Machine Learning
"""
import streamlit as st
from components.banners import render_medical_disclaimer

def render():
    st.markdown("""<div style="margin-bottom: 32px;">
<div class="pro-badge">
<span class="pro-pulse-dot" style="background: #38BDF8; box-shadow: 0 0 10px #38BDF8;"></span> ACADEMIC SPECIFICATIONS &bull; SOP AUDIT
</div>
<h1 style="font-size: 38px; font-weight: 800; color: #FFFFFF; letter-spacing: -1px; margin: 0 0 10px 0;">
About <span class="hero-heading-highlight">CardioPredict</span>
</h1>
<p style="font-size: 15px; color: #94A3B8; max-width: 780px; line-height: 1.6; margin: 0;">
Undergraduate Machine Learning Project engineered strictly in accordance with Darshan University Computer Engineering Department ML Project Standard Operating Procedure (SOP).
</p>
</div>""", unsafe_allow_html=True)

    # Academic Motivation Card
    st.markdown("""<div class="vercel-card" style="margin-bottom: 24px; border-left: 3px solid #38BDF8; padding: 26px 30px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
<span style="font-size: 20px;">🎯</span>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">Clinical Motivation & Project Objective</span>
</div>
<p style="font-size: 14px; color: #94A3B8; line-height: 1.7; margin-bottom: 14px;">
Cardiovascular diseases (CVDs) remain the world's leading cause of premature mortality, claiming an estimated 17.9 million lives each year according to the World Health Organization (WHO). In traditional diagnostic pathways, conditions like asymptomatic arterial hypertension and progressive coronary plaque deposition develop silently without overt physical symptoms.
</p>
<p style="font-size: 14px; color: #94A3B8; line-height: 1.7; margin: 0;">
The objective of <b>CardioPredict</b> is to demonstrate how supervised ensemble machine learning—specifically <b style="color: #F43F5E;">Random Forest</b> and <b style="color: #38BDF8;">AdaBoost</b>—can identify high-risk non-linear interactions across routine, non-invasive vital signs and laboratory markers. By providing instantaneous pre-screening triage, this platform assists clinical practitioners in prioritizing diagnostic resources.
</p>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""<div class="vercel-card" style="height: 100%; padding: 26px 28px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px;">
<span style="font-size: 20px;">⚙️</span>
<span style="font-size: 17px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">Full-Stack ML Technology Stack</span>
</div>
<div style="display: flex; flex-direction: column; gap: 12px; font-size: 13.5px;">
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Core Environment</span>
<span style="font-weight: 700; color: #FFFFFF;">Python 3.10+ / 3.13</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Machine Learning</span>
<span style="font-weight: 700; color: #FFFFFF;">Scikit-learn, Joblib, NumPy</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Data Wrangling & Pipeline</span>
<span style="font-weight: 700; color: #FFFFFF;">Pandas, Standard Scaler</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Interactive UI/UX</span>
<span style="font-weight: 700; color: #FFFFFF;">Streamlit 1.51 + Custom CSS</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Visual Telemetry</span>
<span style="font-weight: 700; color: #FFFFFF;">Plotly Interactive Charts</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center;">
<span style="color: #94A3B8;">REST API Microservice</span>
<span style="font-weight: 700; color: #FFFFFF;">FastAPI, Pydantic, Uvicorn</span>
</div>
</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="vercel-card" style="height: 100%; padding: 26px 28px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px;">
<span style="font-size: 20px;">📊</span>
<span style="font-size: 17px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">Empirical Cohort & Model Benchmarks</span>
</div>
<div style="display: flex; flex-direction: column; gap: 12px; font-size: 13.5px;">
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Clinical Dataset</span>
<span style="font-weight: 700; color: #FFFFFF;">Cardiovascular Examination Cohort</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Patient Records</span>
<span style="font-weight: 700; color: #FFFFFF;">70,000 Verified Encounters</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Biomarker Feature Vector</span>
<span style="font-weight: 700; color: #FFFFFF;">11 Clinical Features</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Primary Model</span>
<span style="font-weight: 700; color: #10B981;">Random Forest Tuned (73.1% Acc)</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
<span style="color: #94A3B8;">Secondary Model</span>
<span style="font-weight: 700; color: #38BDF8;">AdaBoost Classifier (72.5% Acc)</span>
</div>
<div style="display: flex; justify-content: space-between; align-items: center;">
<span style="color: #94A3B8;">Cross-Validation</span>
<span style="font-weight: 700; color: #FFFFFF;">5-Fold Stratified CV (73.0% Mean)</span>
</div>
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

    # Author Credentials & Academic Context (Dark Slate Glassmorphic Card)
    st.markdown("""<div class="vercel-card" style="text-align: center; padding: 34px 24px; position: relative; overflow: hidden;">
<div style="width: 52px; height: 52px; border-radius: 14px; background: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%); display: inline-flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(225,29,72,0.5); margin-bottom: 16px;">
🎓
</div>
<div style="font-size: 22px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.5px; margin-bottom: 4px;">
Darshan University
</div>
<div style="font-size: 14.5px; font-weight: 600; color: #F43F5E; margin-bottom: 14px;">
Department of Computer Engineering &bull; Semester 5 Machine Learning
</div>
<p style="font-size: 14px; color: #CBD5E1; max-width: 580px; margin: 0 auto 20px auto; line-height: 1.6;">
Student Developer: <b style="color: #FFFFFF; font-size: 15px;">Veerbhadrasinh</b><br>
Academic Year: <span style="color: #94A3B8;">2025–2026</span> &bull; Course Project: Cardiovascular Disease Prediction
</p>
<div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
<span class="trust-tag">✅ Data Cleaning &amp; IQR Outlier Removal</span>
<span class="trust-tag">✅ Dual Ensemble Training (RF &amp; AdaBoost)</span>
<span class="trust-tag">✅ Overfitting Verification &amp; Tuning</span>
<span class="trust-tag">✅ 5-Fold Stratified Cross-Validation</span>
<span class="trust-tag">✅ High-Performance Interactive UI</span>
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    render_medical_disclaimer()
