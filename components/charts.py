"""
CardioPredict Plotly Interactive Chart Components.
Renders Risk Gauge, BMI Visual Indicator, Overfitting Bar Chart, and 5-Fold Cross Validation Chart.
Adapted for modern dark slate aesthetic matching https://heart-disease-prediction-using-mach.vercel.app/
"""
import streamlit as st
import plotly.graph_objects as go

def render_risk_gauge(probability: float):
    """
    Renders a semi-circular Plotly speedometer risk gauge.
    probability is between 0.0 and 1.0.
    """
    pct = round(probability * 100, 1)

    if pct < 45:
        bar_color = "#10B981"  # Emerald
        status_text = "LOW RISK"
    elif pct < 60:
        bar_color = "#F59E0B"  # Amber
        status_text = "MODERATE RISK"
    else:
        bar_color = "#E11D48"  # Crimson / Coral
        status_text = "ELEVATED RISK"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=pct,
        number={
            'suffix': "%",
            'font': {'size': 44, 'color': '#FFFFFF', 'family': 'Inter'}
        },
        title={
            'text': f"<b>{status_text}</b><br><span style='font-size:12px; color:#94A3B8;'>AI Probability Score</span>",
            'font': {'size': 16, 'color': bar_color, 'family': 'Inter'}
        },
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#334155", 'tickfont': {'color': '#94A3B8', 'size': 11}},
            'bar': {'color': bar_color, 'thickness': 0.28},
            'bgcolor': "#1E293B",
            'borderwidth': 0,
            'steps': [
                {'range': [0, 45], 'color': "rgba(16, 185, 129, 0.15)"},
                {'range': [45, 60], 'color': "rgba(245, 158, 11, 0.15)"},
                {'range': [60, 100], 'color': "rgba(225, 29, 72, 0.20)"}
            ],
            'threshold': {
                'line': {'color': "#E11D48", 'width': 3},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "#F8FAFC", 'family': "Inter"},
        height=260,
        margin=dict(l=25, r=25, t=35, b=10)
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

def render_bmi_indicator(bmi: float):
    """
    Renders an interactive horizontal visual BMI spectrum with needle pointer.
    Ranges: Underweight (<18.5) | Normal (18.5-24.9) | Overweight (25-29.9) | Obesity (>=30)
    """
    clamped_bmi = max(12.0, min(bmi, 42.0))
    pos_pct = max(2.0, min(98.0, ((clamped_bmi - 12.0) / (42.0 - 12.0)) * 100.0))

    if bmi < 18.5:
        category = "Underweight"
        cat_color = "#38BDF8"
        badge_bg = "rgba(56, 189, 248, 0.15)"
        badge_border = "#0284C7"
    elif bmi <= 24.9:
        category = "Normal Weight"
        cat_color = "#10B981"
        badge_bg = "rgba(16, 185, 129, 0.15)"
        badge_border = "#059669"
    elif bmi <= 29.9:
        category = "Overweight"
        cat_color = "#F59E0B"
        badge_bg = "rgba(245, 158, 11, 0.15)"
        badge_border = "#D97706"
    else:
        category = "Obesity"
        cat_color = "#E11D48"
        badge_bg = "rgba(225, 29, 72, 0.15)"
        badge_border = "#BE123C"

    html_content = f"""<div style="background: #0F172A; border: 1px solid #1E293B; border-radius: 14px; padding: 16px 20px; margin-top: 10px; margin-bottom: 20px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
<div>
<span style="font-size: 11px; text-transform: uppercase; color: #94A3B8; letter-spacing: 0.5px; font-weight: 700;">Calculated BMI</span>
<span style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin-left: 8px; font-family: monospace;">{bmi:.1f} kg/m²</span>
</div>
<div style="background: {badge_bg}; color: {cat_color}; border: 1px solid {badge_border}; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700;">
{category}
</div>
</div>
<div style="position: relative; height: 10px; border-radius: 6px; background: linear-gradient(90deg, #38BDF8 0%, #10B981 25%, #F59E0B 60%, #E11D48 100%); margin: 16px 0 10px 0;">
<div style="position: absolute; top: -5px; left: {pos_pct}%; transform: translateX(-50%); width: 20px; height: 20px; background: #090D16; border: 3px solid {cat_color}; border-radius: 50%; box-shadow: 0 0 10px {cat_color};"></div>
</div>
<div style="display: flex; justify-content: space-between; font-size: 11px; color: #94A3B8; font-weight: 600;">
<span>Underweight (&lt;18.5)</span>
<span>Normal (18.5-24.9)</span>
<span>Overweight (25-29.9)</span>
<span>Obese (&ge;30)</span>
</div>
</div>"""
    st.markdown(html_content, unsafe_allow_html=True)

def render_overfitting_chart(train_score: float, test_score: float):
    """
    Renders comparative bar chart highlighting the overfitting score gap.
    """
    fig = go.Figure()
    categories = ['Training Score', 'Testing Score']
    scores = [train_score, test_score]
    colors = ['#E11D48', '#10B981']

    fig.add_trace(go.Bar(
        x=categories,
        y=scores,
        marker=dict(color=colors, line=dict(color='#334155', width=1)),
        text=[f"{s:.2f}%" for s in scores],
        textposition='outside',
        textfont=dict(color='#F8FAFC', size=13, family='Inter')
    ))

    gap = train_score - test_score
    fig.update_layout(
        title=dict(text=f"Score Gap: {gap:.2f}% (Overfitting Demonstration)", font=dict(color='#F8FAFC', size=15)),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8", family="Inter"),
        yaxis=dict(
            range=[0, 115],
            gridcolor="#1E293B",
            title="Accuracy (%)"
        ),
        xaxis=dict(gridcolor="rgba(0,0,0,0)"),
        height=280,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

def render_cv_chart(cv_scores: list[float]):
    """Renders 5-fold cross-validation fold-by-fold chart."""
    folds = [f"Fold {i+1}" for i in range(len(cv_scores))]
    mean_val = sum(cv_scores) / len(cv_scores)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=folds,
        y=cv_scores,
        marker=dict(color="#E11D48", line=dict(color="#FB7185", width=1)),
        text=[f"{s:.2f}%" for s in cv_scores],
        textposition='outside',
        textfont=dict(color='#F8FAFC', size=12, family='Inter'),
        name="Fold Accuracy"
    ))

    fig.add_hline(
        y=mean_val,
        line_dash="dash",
        line_color="#10B981",
        annotation_text=f"Mean: {mean_val:.2f}%",
        annotation_position="bottom right",
        annotation_font_color="#10B981"
    )

    fig.update_layout(
        title=dict(text="5-Fold Cross Validation Consistency (Train Data)", font=dict(color='#F8FAFC', size=15)),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94A3B8", family="Inter"),
        yaxis=dict(
            range=[65, 80],
            gridcolor="#1E293B",
            title="Accuracy (%)"
        ),
        xaxis=dict(gridcolor="rgba(0,0,0,0)"),
        height=280,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
