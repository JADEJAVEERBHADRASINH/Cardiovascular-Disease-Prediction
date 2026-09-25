"""
Page: Features
Detailed breakdown of CardioPredict platform features and model capabilities.
"""
import streamlit as st
from components.banners import render_medical_disclaimer

def render():
    st.markdown("""
    <div id="features" style="padding-top: 10px;"></div>
    <div style="text-align: center; max-width: 800px; margin: 0 auto 36px auto;">
        <div class="ref-hero-pill">
            <span style="color: #20D9C2; font-size: 14px;">✨</span>
            <span>Platform Capabilities</span>
        </div>
        <h2 style="font-size: 40px; font-weight: 800; color: #F8FAFC; margin: 0 0 12px 0; letter-spacing: -1px;">
            Why Choose <span class="text-primary-glow">CardioPredict?</span>
        </h2>
        <p style="font-size: 16px; color: #94A3B8; margin: 0; line-height: 1.6;">
            Our platform combines cutting-edge machine learning technology with clinical data integrity to deliver reliable cardiovascular risk insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    features = [
        ("🧠", "Advanced ML Models", "Choose between AdaBoost and Random Forest algorithms trained and cross-validated on 70,000 patient records.", "Ensemble Learning"),
        ("⚡", "Instant Results", "Get your cardiovascular risk assessment in seconds, not days. Real-time inference with no waiting for laboratory reports.", "< 50ms Latency"),
        ("🛡️", "Data Secure", "Your health data is processed in-memory securely with zero permanent database storage. Your privacy is our priority.", "Zero Retention"),
        ("📋", "11 Risk Factors", "Comprehensive multi-signal analysis covering age, gender, BMI, systolic/diastolic blood pressure, cholesterol, glucose, and lifestyle.", "Multi-Dimensional"),
        ("📈", "73% Accuracy", "Our models have been rigorously evaluated with 5-fold cross validation on real-world cardiovascular disease clinical encounters.", "Cross-Validated"),
        ("🔒", "Privacy First", "Client data is processed strictly in real-time with zero third-party tracking, analytics cookies, or external transmission.", "100% Private")
    ]

    col1, col2, col3 = st.columns(3)
    for i, (icon, title, desc, tag) in enumerate(features):
        target_col = [col1, col2, col3][i % 3]
        with target_col:
            st.markdown(f"""
            <div class="ref-feature-box" style="height: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div class="ref-feature-icon" style="margin-bottom: 0;">{icon}</div>
                    <span style="font-size: 11px; font-weight: 700; color: #20D9C2; background: rgba(20, 184, 166, 0.12); padding: 3px 8px; border-radius: 6px; border: 1px solid rgba(20, 184, 166, 0.25);">
                        {tag}
                    </span>
                </div>
                <div style="font-size: 17px; font-weight: 700; color: #F8FAFC; margin-bottom: 8px;">{title}</div>
                <div style="font-size: 13px; color: #94A3B8; line-height: 1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

    # Secondary Features Deep Dive
    st.markdown("""
    <div class="ref-card">
        <h3 style="font-size: 20px; font-weight: 700; color: #F8FAFC; margin-bottom: 12px;">
            🔬 Clinical Explainability & Feature Attribution
        </h3>
        <p style="font-size: 14px; color: #94A3B8; line-height: 1.7; margin-bottom: 18px;">
            Unlike black-box models, CardioPredict calculates the specific physiological drivers elevating an individual patient's score. Systolic and diastolic readings, body mass index, serum cholesterol, and self-reported physical habits are benchmarked against American Heart Association (AHA) clinical cutoffs.
        </p>
        <div style="display: flex; gap: 14px; flex-wrap: wrap;">
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 18px; font-size: 13px;">
                <b style="color: #20D9C2;">Hemodynamic Staging:</b> Automatic classification of Normal, Elevated, Stage 1, Stage 2, and Crisis BP
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 18px; font-size: 13px;">
                <b style="color: #20D9C2;">Live BMI Meter:</b> Real-time visual indicator showing position across Underweight, Normal, Overweight, and Obese
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_medical_disclaimer()
