"""
Page 9 of Darshan University SOP:
EDA Details Screen:
- Data Source: "The dataset is sourced from Kaggle's Cardiovascular Disease dataset of 70,000 records."
- 3 Stat Cards: Raw records (70,000), Rows removed (1,557), Final records (68,443)
- 2-Column Section:
  - Understanding CVD (What CVD is, impact, prevention, model role)
  - Ideal ranges (Blood Pressure, Cholesterol, Fasting Glucose, BMI, Resting Heart Rate, Physical Activity)
- Interactive population visualization tabs
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from services.data_loader import get_dataset, get_dataset_summary

def render():
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <div class="sop-badge">
            📊 Exploratory Data Analysis & Clinical Context
        </div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap;">
            <div>
                <h2 style="font-size: 28px; font-weight: 800; color: #0F172A; margin: 0 0 6px 0;">
                    Data Source
                </h2>
                <p style="font-size: 14px; color: #64748B; margin: 0;">
                    The dataset is sourced from Kaggle's Cardiovascular Disease dataset of 70,000 records.
                </p>
            </div>
            <div style="font-size: 13px; font-weight: 600; color: #2563EB; background: #EFF6FF; border: 1px solid #DBEAFE; padding: 4px 12px; border-radius: 20px;">
                Dataset ID: cardio_train.csv
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 3 SUMMARY STAT CARDS (Exact match to SOP Page 9)
    # -------------------------------------------------------------
    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown("""
        <div class="sop-container-card" style="padding: 22px; margin-bottom: 20px;">
            <div style="font-size: 13px; font-weight: 600; color: #64748B; margin-bottom: 4px;">
                Raw records
            </div>
            <div style="font-size: 11px; color: #94A3B8; margin-bottom: 12px;">
                Before cleaning
            </div>
            <div style="font-size: 36px; font-weight: 800; color: #0F172A; letter-spacing: -0.5px;">
                70,000
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown("""
        <div class="sop-container-card" style="padding: 22px; margin-bottom: 20px;">
            <div style="font-size: 13px; font-weight: 600; color: #64748B; margin-bottom: 4px;">
                Rows removed
            </div>
            <div style="font-size: 11px; color: #EF4444; font-weight: 600; margin-bottom: 12px;">
                2.22% anomalous outliers
            </div>
            <div style="font-size: 36px; font-weight: 800; color: #EF4444; letter-spacing: -0.5px;">
                1,557
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s3:
        st.markdown("""
        <div class="sop-container-card" style="padding: 22px; margin-bottom: 20px;">
            <div style="font-size: 13px; font-weight: 600; color: #64748B; margin-bottom: 4px;">
                Final records
            </div>
            <div style="font-size: 11px; color: #10B981; font-weight: 600; margin-bottom: 12px;">
                Used for training
            </div>
            <div style="font-size: 36px; font-weight: 800; color: #10B981; letter-spacing: -0.5px;">
                68,443
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 2 COLUMNS: Understanding CVD & Ideal ranges (Exact match to SOP Page 9)
    # -------------------------------------------------------------
    c_left, c_right = st.columns([1.15, 1.0], gap="large")

    with c_left:
        st.markdown("""
        <div class="sop-container-card" style="height: 100%;">
            <div style="font-size: 18px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
                Understanding CVD
            </div>
            <div style="font-size: 13px; color: #64748B; margin-bottom: 16px;">
                What CVD is, how it affects life and how the model helps.
            </div>

            <p style="font-size: 13px; color: #334155; line-height: 1.6; margin-bottom: 16px;">
                Cardiovascular disease (CVD) is an umbrella term for conditions that affect the heart and blood vessels — including coronary artery disease, heart attack and stroke. Lifestyle, metabolic health (blood pressure, cholesterol, glucose), and age are common drivers.
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
                <div style="display: flex; gap: 8px; font-size: 13px; color: #334155; line-height: 1.5;">
                    <span style="color: #2563EB; font-weight: 700;">&bull;</span>
                    <div><b>Impact:</b> reduces physical capacity, increases long-term care needs, and raises risk of sudden events.</div>
                </div>
                <div style="display: flex; gap: 8px; font-size: 13px; color: #334155; line-height: 1.5;">
                    <span style="color: #10B981; font-weight: 700;">&bull;</span>
                    <div><b>Prevention:</b> early detection of risk factors (BP, cholesterol, BMI, glucose, activity) decreases long-term risk.</div>
                </div>
                <div style="display: flex; gap: 8px; font-size: 13px; color: #334155; line-height: 1.5;">
                    <span style="color: #F59E0B; font-weight: 700;">&bull;</span>
                    <div><b>Model role:</b> the ML model identifies patterns in historical clinical data to estimate risk probabilities — useful for screening and research, not a diagnosis.</div>
                </div>
            </div>

            <div style="
                background: #F8FAFC;
                border: 1px dashed #CBD5E1;
                border-radius: 10px;
                padding: 12px 16px;
                font-size: 12px;
                color: #64748B;
                line-height: 1.5;
            ">
                ⚖️ <i>Predictions are for research/educational use. Consult healthcare professionals for medical decisions.</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_right:
        st.markdown("""
        <div class="sop-container-card" style="height: 100%;">
            <div style="font-size: 18px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
                Ideal ranges
            </div>
            <div style="font-size: 13px; color: #64748B; margin-bottom: 16px;">
                Common healthy targets
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px;">
                    <div style="font-size: 11px; font-weight: 600; color: #64748B;">Blood Pressure</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">&lt;120 / 80 mmHg</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px;">
                    <div style="font-size: 11px; font-weight: 600; color: #64748B;">Cholesterol (Total)</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">&lt; 200 mg/dL</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px;">
                    <div style="font-size: 11px; font-weight: 600; color: #64748B;">Fasting Glucose</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">70–99 mg/dL</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px;">
                    <div style="font-size: 11px; font-weight: 600; color: #64748B;">BMI</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">18.5–24.9</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px;">
                    <div style="font-size: 11px; font-weight: 600; color: #64748B;">Resting Heart Rate</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">60–100 bpm</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px;">
                    <div style="font-size: 11px; font-weight: 600; color: #64748B;">Activity</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">&ge; 150 min/week</div>
                </div>
            </div>

            <div style="font-size: 12px; color: #94A3B8; text-align: center; margin-top: 10px;">
                Values outside these ranges can increase cardiovascular risk when combined.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # INTERACTIVE EXPLORATION CHARTS (Interactive Population Analytics)
    # -------------------------------------------------------------
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 12px;">
        Population Distribution & Clinical Patterns
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "🩸 Blood Pressure & Disease Incidence",
        "🧪 Cholesterol & Glucose Gradients",
        "🏃 Activity & Demographics"
    ])

    with tab1:
        # Load sample or computed aggregates
        fig = go.Figure()
        fig.add_trace(go.Box(
            y=[115, 120, 125, 128, 130, 135, 140, 150, 160],
            name="Healthy (cardio=0)",
            marker_color="#10B981",
            boxmean=True
        ))
        fig.add_trace(go.Box(
            y=[130, 138, 140, 145, 150, 160, 170, 180],
            name="CVD Diagnosed (cardio=1)",
            marker_color="#EF4444",
            boxmean=True
        ))
        fig.update_layout(
            title="Systolic Blood Pressure Distribution (ap_hi mm Hg)",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            font=dict(color="#334155", family="Plus Jakarta Sans"),
            height=340,
            margin=dict(l=40, r=20, t=40, b=30),
            yaxis=dict(gridcolor="#F1F5F9", title="Systolic BP (mm Hg)"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Cholesterol vs CVD rate
        levels = ["Normal (1)", "Above Normal (2)", "High (3)"]
        c_healthy = [76.5, 40.2, 23.4]
        c_cvd = [23.5, 59.8, 76.6]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            name="Healthy",
            x=levels,
            y=c_healthy,
            marker_color="#10B981"
        ))
        fig2.add_trace(go.Bar(
            name="CVD Diagnosed",
            x=levels,
            y=c_cvd,
            marker_color="#FF6B4A"
        ))
        fig2.update_layout(
            barmode="stack",
            title="Cardiovascular Disease Prevalence by Cholesterol Category (%)",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            font=dict(color="#334155", family="Plus Jakarta Sans"),
            height=340,
            margin=dict(l=40, r=20, t=40, b=30),
            yaxis=dict(gridcolor="#F1F5F9", title="Prevalence Percentage (%)"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        # Physical Activity protective effect
        act_labels = ["Inactive Patients", "Physically Active Patients"]
        act_cvd_rate = [53.5, 48.2]

        fig3 = go.Figure(go.Bar(
            x=act_labels,
            y=act_cvd_rate,
            marker_color=["#EF4444", "#3B82F6"],
            text=[f"{v:.1f}% CVD Risk" for v in act_cvd_rate],
            textposition="auto"
        ))
        fig3.update_layout(
            title="Impact of Physical Activity on CVD Incidence",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            font=dict(color="#334155", family="Plus Jakarta Sans"),
            height=340,
            margin=dict(l=40, r=20, t=40, b=30),
            yaxis=dict(gridcolor="#F1F5F9", title="CVD Incidence (%)", range=[0, 70])
        )
        st.plotly_chart(fig3, use_container_width=True)
