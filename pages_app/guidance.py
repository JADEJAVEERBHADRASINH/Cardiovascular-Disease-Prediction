"""
CardioPredict Health Guidance Page.
Evidence-based lifestyle education covering the 7 modifiable cardiovascular health domains:
Blood Pressure, Cholesterol, Physical Activity, Smoking, Alcohol, Weight/BMI, and Healthy Nutrition.
Includes mandatory educational disclaimer and clinical targets.
"""
import streamlit as st
from components.banners import render_medical_disclaimer

def render():
    st.markdown("""<div style="margin-bottom: 32px;">
<div class="pro-badge">
<span class="pro-pulse-dot" style="background: #10B981; box-shadow: 0 0 10px #10B981;"></span> CLINICAL LIFESTYLE PROTOCOLS
</div>
<h1 style="font-size: 38px; font-weight: 800; color: #FFFFFF; letter-spacing: -1px; margin: 0 0 10px 0;">
Cardiovascular <span class="hero-heading-highlight">Health Guidance</span>
</h1>
<p style="font-size: 15px; color: #94A3B8; max-width: 760px; line-height: 1.6; margin: 0;">
Evidence-based clinical guidelines derived from the American Heart Association (AHA) and European Society of Cardiology (ESC). Discover how modifiable biomarkers impact vascular integrity and long-term myocardial health.
</p>
</div>""", unsafe_allow_html=True)

    # 4 Quick Health Target Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 32px;">&lt;120/80</div>
<div class="stat-counter-label">Optimal BP Target</div>
<div style="font-size: 11px; color: #64748B; margin-top: 4px;">Systolic / Diastolic mmHg</div>
</div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 32px;">18.5–24.9</div>
<div class="stat-counter-label">Healthy BMI Range</div>
<div style="font-size: 11px; color: #64748B; margin-top: 4px;">kg/m² Normal Weight</div>
</div>""", unsafe_allow_html=True)
    with m3:
        st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 32px;">≥150m</div>
<div class="stat-counter-label">Weekly Exercise</div>
<div style="font-size: 11px; color: #64748B; margin-top: 4px;">Moderate aerobic exertion</div>
</div>""", unsafe_allow_html=True)
    with m4:
        st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 32px;">0 Cigs</div>
<div class="stat-counter-label">Tobacco Abstinence</div>
<div style="font-size: 11px; color: #64748B; margin-top: 4px;">100% Smoke-free lifestyle</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)

    # 7 Clinical Domains in High-End Glassmorphic Cards
    guidelines = [
        (
            "❤️ Arterial Blood Pressure Regulation",
            "Target: < 120 / 80 mmHg",
            "Systolic pressure reflects arterial wall tension during ventricular ejection. Sustained elevation above 130 mmHg causes mechanical strain on endothelial cells, accelerates arterial stiffening, and triggers left ventricular hypertrophy. Keep sodium intake below 2,300 mg/day, maintain consistent restorative sleep, and prioritize stress mitigation.",
            "#F43F5E",
            "Vital Sign"
        ),
        (
            "🧪 Serum Cholesterol & Lipid Transport",
            "Target: Normal Lipid Thresholds",
            "Excess circulating low-density lipoprotein (LDL) particles infiltrate vascular subendothelial spaces, oxidize, and provoke foam cell inflammatory cascades that form atherosclerotic plaques. Emphasize plant sterols, monounsaturated fats (extra virgin olive oil, avocados), and soluble fiber while eliminating industrial trans-fats.",
            "#38BDF8",
            "Biochemical"
        ),
        (
            "⚖️ Body Mass Index (BMI) & Adiposity",
            "Target: BMI 18.5 – 24.9 kg/m²",
            "Central and visceral adiposity acts as an active endocrine organ, secreting inflammatory cytokines (IL-6, TNF-alpha) that impair vascular dilation and exacerbate insulin resistance. Pair progressive energy equilibrium with unprocessed whole foods for sustainable visceral fat reduction.",
            "#F59E0B",
            "Anthropometric"
        ),
        (
            "🚭 Tobacco Combustion & Nicotine Abstinence",
            "Target: Complete Abstinence (0 Cigarettes/day)",
            "Combustion particulates deliver carbon monoxide that directly displaces oxygen from hemoglobin, while nicotine stimulates sympathetic overdrive and acute endothelial injury. Cessation cuts excess myocardial infarction hazard by 50% within just 12 months.",
            "#EF4444",
            "Lifestyle"
        ),
        (
            "🏃 Sustained Aerobic Physical Conditioning",
            "Target: ≥ 150 Min/week Moderate Activity",
            "Cardiovascular exercise activates endothelial nitric oxide synthase (eNOS), promoting vasodilation, lowering resting vagal tone, and improving lipid clearance. Brisk walking for 30 minutes daily 5 days per week provides optimal cardioprotective benefit.",
            "#10B981",
            "Habitual"
        ),
        (
            "🍷 Alcohol Consumption Discipline",
            "Target: Zero or Minimal Intake",
            "Regular or binge alcohol exposure contributes to toxic cardiomyopathy, supraventricular arrhythmias (holiday heart syndrome), and systemic hypertension. Eliminating excess intake safeguards cardiac stroke volume and hepatic lipid regulation.",
            "#A855F7",
            "Toxicological"
        ),
        (
            "🥗 Cardioprotective Dietary Regimen",
            "Target: Mediterranean or DASH Architecture",
            "Rich in dietary polyphenols, leafy dark greens, antioxidant berries, legumes, and marine omega-3 fatty acids (salmon, mackerel). Minimizes refined carbohydrates and ultra-processed additives that provoke glycemic spikes and vascular oxidative stress.",
            "#14B8A6",
            "Nutritional"
        )
    ]

    for title, target, desc, color, tag in guidelines:
        st.markdown(f"""<div class="vercel-card" style="margin-bottom: 16px; border-left: 3px solid {color}; padding: 22px 26px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 17px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">{title}</span>
<span style="font-size: 10.5px; font-weight: 700; color: {color}; background: {color}18; border: 1px solid {color}44; padding: 2px 9px; border-radius: 999px;">{tag}</span>
</div>
<div style="font-size: 11.5px; font-weight: 700; color: {color}; background: {color}18; border: 1px solid {color}44; padding: 4px 12px; border-radius: 999px; font-family: 'Plus Jakarta Sans', monospace;">
{target}
</div>
</div>
<p style="font-size: 13.5px; color: #94A3B8; line-height: 1.7; margin: 0;">
{desc}
</p>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    render_medical_disclaimer()
