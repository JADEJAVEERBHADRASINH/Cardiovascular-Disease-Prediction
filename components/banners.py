"""
CardioPredict Banner Components.
Clinical Result Banners and Academic Medical Disclaimers.
Dark theme aesthetic matching https://heart-disease-prediction-using-mach.vercel.app/
"""
import streamlit as st

def render_medical_disclaimer():
    """Renders prominent educational/academic disclaimer required by ML SOP."""
    st.markdown("""<div class="medical-notice-box">
<span style="font-size: 20px; color: #E11D48;">⚖️</span>
<div>
<div style="font-size: 13px; font-weight: 700; color: #F8FAFC; margin-bottom: 2px;">
ACADEMIC SCREENING DISCLAIMER & MEDICAL NOTICE
</div>
<div style="font-size: 12px; color: #94A3B8; line-height: 1.6;">
This application is developed strictly for educational and machine-learning demonstration purposes under the Computer Engineering Department ML Project SOP (Darshan University). The predictions generated are based on statistical patterns from historical data and <b>are not a medical diagnosis or substitute for professional medical advice</b>. Always consult a qualified physician for clinical care.
</div>
</div>
</div>""", unsafe_allow_html=True)

def render_result_banner(risk_label: str, risk_pct: float, model_used: str):
    """Renders clear, honest clinical screening result banner in dark theme."""
    is_elevated = ("ELEVATED" in risk_label.upper() or "HIGH" in risk_label.upper())
    
    if is_elevated:
        card_border = "border: 1px solid #E11D48; background: rgba(225, 29, 72, 0.08); box-shadow: 0 0 24px rgba(225, 29, 72, 0.15);"
        pill_bg = "background: #E11D48; color: #FFFFFF;"
        title_color = "#FB7185"
        title_text = "ELEVATED CARDIOVASCULAR RISK"
        icon_display = "⚠️"
        sub_text = "Entered indicators reflect a heightened statistical probability of cardiovascular disease based on trained classifier patterns. Medical evaluation is advised."
    else:
        card_border = "border: 1px solid #10B981; background: rgba(16, 185, 129, 0.08); box-shadow: 0 0 24px rgba(16, 185, 129, 0.15);"
        pill_bg = "background: #10B981; color: #FFFFFF;"
        title_color = "#34D399"
        title_text = "LOW CARDIOVASCULAR RISK"
        icon_display = "🛡️"
        sub_text = "Entered health indicators fall within non-elevated parameters. Continue maintaining an active and healthy lifestyle."

    st.markdown(f"""
    <div style="{card_border} border-radius: 16px; padding: 26px; text-align: center; margin-bottom: 24px;">
        <div style="font-size: 32px; margin-bottom: 8px;">{icon_display}</div>
        <div style="display: inline-block; {pill_bg} font-size: 12px; font-weight: 800; padding: 4px 14px; border-radius: 20px; letter-spacing: 0.5px; margin-bottom: 12px;">
            AI PREDICTION &bull; {risk_pct}% RISK PROBABILITY
        </div>
        <div style="font-size: 26px; font-weight: 800; color: {title_color}; margin-bottom: 8px; letter-spacing: -0.5px;">
            {title_text}
        </div>
        <div style="font-size: 14px; color: #94A3B8; max-width: 620px; margin: 0 auto 14px auto; line-height: 1.6;">
            {sub_text}
        </div>
        <div style="font-size: 11.5px; color: #64748B;">
            Screening Model: <span style="color: #F8FAFC; font-weight: 600;">{model_used}</span> &bull; Sub-10ms In-Process Inference
        </div>
    </div>
    """, unsafe_allow_html=True)
