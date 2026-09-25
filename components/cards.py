"""
CardioPredict Reusable Card Components.
MetricCard, FactorPill, PipelineStageCard, and FeatureCard.
Pro-grade dark glassmorphism matching modern SaaS interfaces.
"""
import streamlit as st

def render_metric_card(title: str, value: str, subtext: str = "", badge_text: str = "", badge_color: str = "#E11D48"):
    """Renders a sleek dark stat counter card."""
    st.markdown(f"""
    <div class="stat-counter-card">
        <div class="stat-counter-num">{value}</div>
        <div class="stat-counter-label">{title}</div>
        {f'<div style="font-size: 12px; color: #64748B; margin-top: 4px;">{subtext}</div>' if subtext else ''}
        {f'<div style="margin-top: 8px;"><span style="font-size: 11px; font-weight: 700; color: {badge_color}; background: rgba(225,29,72,0.12); border: 1px solid rgba(225,29,72,0.3); padding: 2px 8px; border-radius: 12px;">{badge_text}</span></div>' if badge_text else ''}
    </div>
    """, unsafe_allow_html=True)

def render_factor_pill(factor: dict):
    """Renders an individual factor impact card with glassmorphism."""
    color = factor.get("color", "#E11D48")
    icon = factor.get("icon", "🔹")
    name = factor.get("name", "Factor")
    val = factor.get("value", "")
    impact = factor.get("impact", "")

    st.markdown(f"""<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 14px 16px; margin-bottom: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25); backdrop-filter: blur(8px);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<span style="font-size: 16px;">{icon}</span>
<span style="background: {color}22; color: {color}; border: 1px solid {color}66; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 20px;">
{impact}
</span>
</div>
<div style="font-size: 14px; font-weight: 700; color: #FFFFFF; letter-spacing: -0.2px;">{name}</div>
<div style="font-size: 12.5px; color: #94A3B8; margin-top: 3px;">{val}</div>
</div>""", unsafe_allow_html=True)

def render_feature_card(icon: str, title: str, description: str):
    """Renders a feature card for the 'Why Choose CardioPredict' grid."""
    st.markdown(f"""
    <div class="vercel-card">
        <div class="vercel-card-icon-box">
            {icon}
        </div>
        <div class="vercel-card-title">{title}</div>
        <p class="vercel-card-desc">{description}</p>
    </div>
    """, unsafe_allow_html=True)

def render_how_it_works_step(step_number: str, title: str, description: str):
    """Renders a numbered step circle for 'How It Works'."""
    st.markdown(f"""
    <div style="text-align: center; padding: 12px;">
        <div class="step-circle-outer">
            <span style="font-size: 28px; color: #F43F5E;">❤️</span>
            <div class="step-circle-badge">{step_number}</div>
        </div>
        <div style="font-size: 18.5px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px; letter-spacing: -0.3px;">
            {title}
        </div>
        <p style="font-size: 13.5px; color: #94A3B8; line-height: 1.65; margin: 0 auto; max-width: 290px;">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_pipeline_card(step_num: int, title: str, subtitle: str, bullets: list[str]):
    """Renders a stage in the ML pipeline flowchart."""
    bullet_items = "".join([f"<li style='margin-bottom: 6px; color: #94A3B8;'>{b}</li>" for b in bullets])
    st.markdown(f"""
    <div class="vercel-card" style="padding: 22px 26px; margin-bottom: 18px;">
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 14px;">
            <div style="
                width: 36px;
                height: 36px;
                border-radius: 10px;
                background: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%);
                color: #FFFFFF;
                font-weight: 800;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 15px;
                box-shadow: 0 0 14px rgba(225, 29, 72, 0.45);
            ">{step_num}</div>
            <div>
                <div style="font-size: 16.5px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">{title}</div>
                <div style="font-size: 12px; color: #F43F5E; font-weight: 600;">{subtitle}</div>
            </div>
        </div>
        <ul style="margin: 0; padding-left: 22px; font-size: 13px; line-height: 1.65;">
            {bullet_items}
        </ul>
    </div>
    """, unsafe_allow_html=True)
