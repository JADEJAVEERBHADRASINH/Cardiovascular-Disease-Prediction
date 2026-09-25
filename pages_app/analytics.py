"""
CardioAI Population Health Analytics Dashboard.
10+ Interactive, clinical visualizations exploring patterns across 70,000 patient encounters.
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from services.data_loader import load_cardio_dataset
from components.banners import render_medical_disclaimer

PLOT_THEME = {
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(15, 23, 42, 0.8)",
    "font": dict(color="#94A3B8", family="Inter", size=12),
    "xaxis": dict(gridcolor="#1E293B", linecolor="#334155"),
    "yaxis": dict(gridcolor="#1E293B", linecolor="#334155"),
    "margin": dict(l=35, r=20, t=40, b=35)
}

def render():
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <div class="vercel-badge">
            <span class="vercel-badge-icon">📊</span> EXPLORATORY DATA ANALYSIS
        </div>
        <h2 style="font-size: 32px; font-weight: 800; color: #FFFFFF; margin: 0 0 6px 0;">
            Cardiovascular Health Analytics
        </h2>
        <p style="font-size: 14px; color: #94A3B8; margin: 0;">
            Comprehensive statistical exploration across 70,000 patient records examining multi-variable cardiovascular disease risk drivers.
        </p>
    </div>
    """, unsafe_allow_html=True)

    df = load_cardio_dataset()
    if df is None:
        st.error("❌ Dataset 'cardio_train.csv' not found. Please ensure the file is present in the project directory.")
        return

    # Filter physiologically plausible subset for hemodynamic visualization clarity
    df_clean = df[
        (df["ap_hi"].between(70, 220)) &
        (df["ap_lo"].between(40, 140)) &
        (df["ap_hi"] > df["ap_lo"]) &
        (df["bmi"].between(15, 50))
    ]

    # Quick Summary Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Cohort Encounters", f"{len(df):,}")
    with c2:
        cvd_rate = (df['cardio'].mean() * 100).round(1)
        st.metric("Overall CVD Prevalence", f"{cvd_rate}%")
    with c3:
        avg_age = df['age_years'].mean().round(1)
        st.metric("Mean Patient Age", f"{avg_age} years")
    with c4:
        avg_bmi = df['bmi'].mean().round(1)
        st.metric("Mean Patient BMI", f"{avg_bmi} kg/m²")

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ROW 1: Target Distribution & Age Density
    # -------------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='cardio-card'><div class='card-title'>1. Target Class Distribution (cardio)</div>", unsafe_allow_html=True)
        counts = df["target_label"].value_counts().reset_index()
        counts.columns = ["Status", "Count"]
        fig1 = px.pie(
            counts, values="Count", names="Status",
            color="Status",
            color_discrete_map={"Healthy (No CVD)": "#10B981", "Cardiovascular Disease": "#EF4444"},
            hole=0.55
        )
        fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#0F172A", family="Plus Jakarta Sans"), height=290, margin=dict(t=20, b=20, l=10, r=10))
        st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>Balanced 50/50 dataset (35,021 Healthy vs 34,979 Diagnosed) prevents learning bias toward the majority class.</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='cardio-card'><div class='card-title'>2. Age Distribution vs Cardiovascular Risk</div>", unsafe_allow_html=True)
        fig2 = px.histogram(
            df_clean, x="age_years", color="target_label",
            nbins=30, barmode="overlay", opacity=0.75,
            color_discrete_map={"Healthy (No CVD)": "#10B981", "Cardiovascular Disease": "#EF4444"},
            labels={"age_years": "Age (Years)", "count": "Patients"}
        )
        fig2.update_layout(**PLOT_THEME, height=290)
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>CVD prevalence escalates markedly past 53-55 years of age due to progressive vascular remodeling.</div></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ROW 2: Gender Breakdown & Hemodynamic Blood Pressure Scatter
    # -------------------------------------------------------------
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("<div class='cardio-card'><div class='card-title'>3. Gender Demographics & Disease Rates</div>", unsafe_allow_html=True)
        gender_agg = df.groupby(["gender_label", "target_label"]).size().reset_index(name="count")
        fig3 = px.bar(
            gender_agg, x="gender_label", y="count", color="target_label",
            barmode="group",
            color_discrete_map={"Healthy (No CVD)": "#10B981", "Cardiovascular Disease": "#EF4444"},
            labels={"gender_label": "Biological Sex", "count": "Patient Count"}
        )
        fig3.update_layout(**PLOT_THEME, height=290)
        st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>Female patients represent ~65% of recorded encounters; however, disease rate is comparable (~50%) across sexes.</div></div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='cardio-card'><div class='card-title'>4. Blood Pressure Hemodynamic Distribution</div>", unsafe_allow_html=True)
        sample_df = df_clean.sample(n=3000, random_state=42)
        fig4 = px.scatter(
            sample_df, x="ap_hi", y="ap_lo", color="target_label",
            opacity=0.65,
            color_discrete_map={"Healthy (No CVD)": "#10B981", "Cardiovascular Disease": "#EF4444"},
            labels={"ap_hi": "Systolic BP (mmHg)", "ap_lo": "Diastolic BP (mmHg)"}
        )
        fig4.update_layout(**PLOT_THEME, height=290)
        st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>Strong clustering of disease-positive cases (red) occurs at systolic BP &gt; 135 mmHg and diastolic &gt; 85 mmHg.</div></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ROW 3: Serum Cholesterol & Fasting Blood Glucose
    # -------------------------------------------------------------
    col5, col6 = st.columns(2)

    with col5:
        st.markdown("<div class='cardio-card'><div class='card-title'>5. Serum Cholesterol & Cardiovascular Risk</div>", unsafe_allow_html=True)
        chol_rate = df.groupby("chol_label")["cardio"].mean().reset_index()
        chol_rate["rate_pct"] = (chol_rate["cardio"] * 100).round(1)
        chol_rate["sort_order"] = chol_rate["chol_label"].map({"Normal": 1, "Above Normal": 2, "High": 3})
        chol_rate = chol_rate.sort_values("sort_order")

        fig5 = px.bar(
            chol_rate, x="chol_label", y="rate_pct",
            text="rate_pct",
            color="chol_label",
            color_discrete_map={"Normal": "#10B981", "Above Normal": "#F59E0B", "High": "#EF4444"},
            labels={"chol_label": "Serum Cholesterol Tier", "rate_pct": "CVD Rate (%)"}
        )
        fig5.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig5.update_layout(**PLOT_THEME, height=290, showlegend=False)
        fig5.update_yaxes(range=[0, 95])
        st.plotly_chart(fig5, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>High cholesterol (Tier 3) exhibits a 76.6% disease incidence, representing a primary cardiovascular risk driver.</div></div>", unsafe_allow_html=True)

    with col6:
        st.markdown("<div class='cardio-card'><div class='card-title'>6. Fasting Glucose Level Impact</div>", unsafe_allow_html=True)
        gluc_rate = df.groupby("gluc_label")["cardio"].mean().reset_index()
        gluc_rate["rate_pct"] = (gluc_rate["cardio"] * 100).round(1)
        gluc_rate["sort_order"] = gluc_rate["gluc_label"].map({"Normal": 1, "Above Normal": 2, "High": 3})
        gluc_rate = gluc_rate.sort_values("sort_order")

        fig6 = px.bar(
            gluc_rate, x="gluc_label", y="rate_pct",
            text="rate_pct",
            color="gluc_label",
            color_discrete_map={"Normal": "#10B981", "Above Normal": "#F59E0B", "High": "#EF4444"},
            labels={"gluc_label": "Glucose Level", "rate_pct": "CVD Rate (%)"}
        )
        fig6.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig6.update_layout(**PLOT_THEME, height=290, showlegend=False)
        fig6.update_yaxes(range=[0, 95])
        st.plotly_chart(fig6, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>Elevated blood glucose correlates with microvascular stress and accelerated plaque development.</div></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ROW 4: Tobacco, Alcohol, BMI, and Physical Activity
    # -------------------------------------------------------------
    col7, col8 = st.columns(2)

    with col7:
        st.markdown("<div class='cardio-card'><div class='card-title'>7. Body Mass Index (BMI) Distribution</div>", unsafe_allow_html=True)
        fig7 = px.box(
            df_clean, x="target_label", y="bmi", color="target_label",
            color_discrete_map={"Healthy (No CVD)": "#10B981", "Cardiovascular Disease": "#EF4444"},
            labels={"target_label": "Cohort", "bmi": "BMI (kg/m²)"}
        )
        fig7.update_layout(**PLOT_THEME, height=290, showlegend=False)
        st.plotly_chart(fig7, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>Median BMI in the diseased cohort shifts upward significantly into overweight and obese clinical ranges.</div></div>", unsafe_allow_html=True)

    with col8:
        st.markdown("<div class='cardio-card'><div class='card-title'>8. Cardioprotective Effect of Physical Activity</div>", unsafe_allow_html=True)
        act_rate = df.groupby("active_label")["cardio"].mean().reset_index()
        act_rate["rate_pct"] = (act_rate["cardio"] * 100).round(1)
        fig8 = px.bar(
            act_rate, x="active_label", y="rate_pct",
            text="rate_pct",
            color="active_label",
            color_discrete_map={"Active": "#10B981", "Inactive": "#EF4444"},
            labels={"active_label": "Activity Status", "rate_pct": "CVD Rate (%)"}
        )
        fig8.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig8.update_layout(**PLOT_THEME, height=290, showlegend=False)
        fig8.update_yaxes(range=[0, 75])
        st.plotly_chart(fig8, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>Patients reporting routine aerobic activity demonstrate lower cardiovascular disease prevalence across all age strata.</div></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ROW 5: Height vs Weight & Correlation Matrix
    # -------------------------------------------------------------
    col9, col10 = st.columns(2)

    with col9:
        st.markdown("<div class='cardio-card'><div class='card-title'>9. Height vs Weight Biometric Correlation</div>", unsafe_allow_html=True)
        sample_hw = df_clean.sample(n=2500, random_state=42)
        fig9 = px.scatter(
            sample_hw, x="height", y="weight", color="target_label",
            opacity=0.6,
            color_discrete_map={"Healthy (No CVD)": "#10B981", "Cardiovascular Disease": "#EF4444"},
            labels={"height": "Height (cm)", "weight": "Weight (kg)"}
        )
        fig9.update_layout(**PLOT_THEME, height=290)
        st.plotly_chart(fig9, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>High body weight relative to stature shows distinct clustering with cardiovascular diagnosis.</div></div>", unsafe_allow_html=True)

    with col10:
        st.markdown("<div class='cardio-card'><div class='card-title'>10. Feature Correlation Matrix with Target</div>", unsafe_allow_html=True)
        corr_cols = ["age_years", "gender", "height", "weight", "ap_hi", "ap_lo", "cholesterol", "gluc", "smoke", "alco", "active", "cardio"]
        corr_matrix = df_clean[corr_cols].corr().round(2)
        fig10 = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="Blues",
            labels=dict(color="Correlation")
        )
        fig10.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#334155", family="Plus Jakarta Sans", size=10),
            height=290,
            margin=dict(l=35, r=20, t=20, b=20)
        )
        st.plotly_chart(fig10, use_container_width=True, config={"displayModeBar": False})
        st.markdown("<div style='font-size: 11px; color: #64748B;'>ap_hi (0.43), age_years (0.24), and cholesterol (0.22) possess highest linear correlation with cardio status.</div></div>", unsafe_allow_html=True)

    render_medical_disclaimer()
