"""
CardioPredict Main Application Page.
Pro-grade medical AI UI/UX matching modern high-end web applications.
Features:
- Ambient pulse-glow hero with illuminated gradient typography & ECG sinus graph
- Fast demo presets for testing (Healthy, Borderline, Hypertensive)
- Dynamic glassmorphic stat counter cards
- Sectioned clinical assessment form with segmented pill switches & live BMI needle gauge
- Live AHA Blood Pressure stage evaluation
- Speedometer risk gauge & factor attribution breakdown
- 'Why Choose CardioPredict?' 6-card feature grid
- 'How It Works' 3-step numbered journey
"""
import streamlit as st
from utils.helpers import calculate_bmi, validate_patient_inputs, analyze_key_factors, classify_blood_pressure
from components.charts import render_risk_gauge, render_bmi_indicator
from components.cards import render_factor_pill, render_feature_card, render_how_it_works_step
from components.banners import render_result_banner, render_medical_disclaimer
from services.predictor import predict_risk

def render():
    # -------------------------------------------------------------
    # 1. HERO SECTION (WITH AMBIENT ILLUMINATION & ECG GRAPHIC)
    # -------------------------------------------------------------
    st.markdown("""
    <div class="hero-glow-bg">
        <div class="hero-glow-blob"></div>
        <div style="text-align: center; position: relative; z-index: 1; padding: 16px 0 10px 0;">
            <div class="pro-badge">
                <span class="pro-pulse-dot"></span> AI-POWERED CARDIAC RISK ASSESSMENT
            </div>
            <h1 class="hero-heading">
                Predict Your <span class="hero-heading-highlight">Heart Disease Risk</span> Instantly
            </h1>
            <p class="hero-description">
                Enter your health metrics below and let our machine learning models analyze your cardiovascular risk in seconds. Based on clinical data from 70,000+ patient examinations.
            </p>
            <!-- Animated ECG Sinus Rhythm Wave -->
            <div style="margin: 22px auto 0 auto; max-width: 540px; opacity: 0.9;">
                <svg viewBox="0 0 600 45" style="width: 100%; height: 32px; stroke: #F43F5E; fill: none; stroke-width: 2.2; stroke-linecap: round; filter: drop-shadow(0 0 8px rgba(225, 29, 72, 0.5));">
                    <path d="M 0 22 L 120 22 L 132 8 L 144 38 L 152 14 L 162 30 L 172 22 L 340 22 L 352 8 L 364 38 L 372 14 L 382 30 L 392 22 L 560 22 L 572 8 L 584 38 L 592 14 L 600 22" />
                </svg>
                <div style="display: flex; justify-content: space-between; font-size: 11px; color: #64748B; font-weight: 600; margin-top: 4px;">
                    <span>Normal Sinus Rhythm Simulation</span>
                    <span>Lead-II Continuous Telemetry</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Trust Badges Row
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; margin-bottom: 34px;">
        <div class="trust-tag">
            <span>🛡️</span> 100% In-Session Privacy
        </div>
        <div class="trust-tag">
            <span>⚡</span> Real-time Analysis (&lt;10ms)
        </div>
        <div class="trust-tag">
            <span>🎯</span> 73.1% Validated Accuracy
        </div>
        <div class="trust-tag">
            <span>🧪</span> 11 Clinical Biomarkers
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4-Column Stat Counters Grid
    stat_c1, stat_c2, stat_c3, stat_c4 = st.columns(4)
    with stat_c1:
        st.markdown("""
        <div class="stat-counter-card">
            <div class="stat-counter-num">70K+</div>
            <div class="stat-counter-label">Records Analyzed</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">Kaggle clinical examination cohort</div>
        </div>
        """, unsafe_allow_html=True)
    with stat_c2:
        st.markdown("""
        <div class="stat-counter-card">
            <div class="stat-counter-num">73%</div>
            <div class="stat-counter-label">Holdout Accuracy</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">5-Fold cross-validation verified</div>
        </div>
        """, unsafe_allow_html=True)
    with stat_c3:
        st.markdown("""
        <div class="stat-counter-card">
            <div class="stat-counter-num">11</div>
            <div class="stat-counter-label">Risk Biomarkers</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">Vitals, anthropometry & lab chemistry</div>
        </div>
        """, unsafe_allow_html=True)
    with stat_c4:
        st.markdown("""
        <div class="stat-counter-card">
            <div class="stat-counter-num">&lt;10ms</div>
            <div class="stat-counter-label">Inference Latency</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">Sub-10ms in-process execution</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 2. HEART DISEASE RISK ASSESSMENT FORM
    # -------------------------------------------------------------
    st.markdown("""
    <div id="assessment-form" style="text-align: center; margin-bottom: 20px;">
        <h2 style="font-size: 32px; font-weight: 800; color: #FFFFFF; margin-bottom: 8px; letter-spacing: -0.5px;">
            Heart Disease Risk Assessment
        </h2>
        <p style="font-size: 15px; color: #94A3B8; max-width: 600px; margin: 0 auto;">
            Fill in patient biometric vitals or use a quick demo preset below:
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Demo Presets
    st.markdown("""
    <div style="margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 12.5px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px;">
            ⚡ Quick-Test Patient Profiles:
        </span>
    </div>
    """, unsafe_allow_html=True)

    pr1, pr2, pr3 = st.columns(3)
    with pr1:
        if st.button("🟢 Profile 1: Healthy Patient (Low Risk)", key="btn_preset_low", use_container_width=True):
            st.session_state["p_age"] = 32
            st.session_state["p_gender"] = "Female"
            st.session_state["p_height"] = 168.0
            st.session_state["p_weight"] = 58.0
            st.session_state["p_ap_hi"] = 112
            st.session_state["p_ap_lo"] = 72
            st.session_state["p_chol"] = 1
            st.session_state["p_gluc"] = 1
            st.session_state["p_smoke"] = "No"
            st.session_state["p_alco"] = "No"
            st.session_state["p_active"] = "Active"
            st.rerun()
    with pr2:
        if st.button("🟡 Profile 2: Borderline Vitals (Moderate)", key="btn_preset_mid", use_container_width=True):
            st.session_state["p_age"] = 52
            st.session_state["p_gender"] = "Male"
            st.session_state["p_height"] = 172.0
            st.session_state["p_weight"] = 82.0
            st.session_state["p_ap_hi"] = 134
            st.session_state["p_ap_lo"] = 86
            st.session_state["p_chol"] = 2
            st.session_state["p_gluc"] = 1
            st.session_state["p_smoke"] = "No"
            st.session_state["p_alco"] = "No"
            st.session_state["p_active"] = "Active"
            st.rerun()
    with pr3:
        if st.button("🔴 Profile 3: Hypertensive Patient (High Risk)", key="btn_preset_high", use_container_width=True):
            st.session_state["p_age"] = 62
            st.session_state["p_gender"] = "Male"
            st.session_state["p_height"] = 174.0
            st.session_state["p_weight"] = 96.0
            st.session_state["p_ap_hi"] = 162
            st.session_state["p_ap_lo"] = 102
            st.session_state["p_chol"] = 3
            st.session_state["p_gluc"] = 2
            st.session_state["p_smoke"] = "Yes"
            st.session_state["p_alco"] = "Yes"
            st.session_state["p_active"] = "Inactive"
            st.rerun()

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    # Main Form Card (Encapsulated in Native Border Container with Pro Theme)
    with st.container(border=True):
        # Model Selector at Top of Form
        col_m1, col_m2 = st.columns([1.8, 1.0])
        with col_m1:
            model_options = [
                ("random_forest", "Random Forest Classifier (73.1% Accuracy - Tuned Ensemble)"),
                ("adaboost", "AdaBoost Classifier (72.5% Accuracy - Adaptive Boosting)")
            ]
            selected_model = st.selectbox(
                "Select Machine Learning Model:",
                model_options,
                format_func=lambda x: x[1],
                index=0,
                help="Choose between Random Forest or AdaBoost to evaluate your risk profile."
            )[0]

        with col_m2:
            st.markdown("""
            <div style="margin-top: 28px; text-align: right;">
                <span style="font-size: 12px; font-weight: 700; color: #F43F5E; background: rgba(225,29,72,0.12); border: 1px solid rgba(225,29,72,0.3); padding: 7px 16px; border-radius: 20px; box-shadow: 0 0 12px rgba(225,29,72,0.15);">
                    11 Clinical Features Analyzed
                </span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # Group 1: Demographics
        st.markdown("<div class='form-group-title'><span>👤</span> Patient Demographics</div>", unsafe_allow_html=True)
        col_demo1, col_demo2 = st.columns(2)
        with col_demo1:
            age = st.number_input(
                "Age (Years)", min_value=18, max_value=105,
                value=int(st.session_state.get("p_age", 50)),
                step=1, help="Patient chronological age in solar years."
            )
        with col_demo2:
            preset_gender = st.session_state.get("p_gender", "Male")
            gender_label = st.radio(
                "Biological Sex", ["Female", "Male"],
                index=0 if preset_gender == "Female" else 1,
                horizontal=True,
                help="Biological sex at birth (Female: 1, Male: 2)."
            )
            gender_val = 1 if gender_label == "Female" else 2

        # Group 2: Body Measurements
        st.markdown("<div class='form-group-title'><span>📏</span> Body Measurements (Anthropometry)</div>", unsafe_allow_html=True)
        col_body1, col_body2 = st.columns(2)
        with col_body1:
            height = st.number_input(
                "Height (cm)", min_value=100.0, max_value=220.0,
                value=float(st.session_state.get("p_height", 165.0)),
                step=1.0, help="Measured height in centimeters."
            )
        with col_body2:
            weight = st.number_input(
                "Weight (kg)", min_value=30.0, max_value=200.0,
                value=float(st.session_state.get("p_weight", 74.0)),
                step=0.5, help="Measured weight in kilograms."
            )

        # Live Dynamic BMI Indicator
        live_bmi = calculate_bmi(weight, height)
        render_bmi_indicator(live_bmi)

        # Group 3: Blood Pressure
        st.markdown("<div class='form-group-title'><span>🩺</span> Blood Pressure (Hemodynamics)</div>", unsafe_allow_html=True)
        col_bp1, col_bp2 = st.columns(2)
        with col_bp1:
            ap_hi = st.number_input(
                "Systolic Blood Pressure (ap_hi in mmHg)",
                min_value=70, max_value=240,
                value=int(st.session_state.get("p_ap_hi", 130)),
                step=1,
                help="Upper blood pressure during heart contraction. Clinical ideal: < 120 mmHg."
            )
            st.caption("Upper pressure during cardiac contraction (Normal: < 120 mmHg)")
        with col_bp2:
            ap_lo = st.number_input(
                "Diastolic Blood Pressure (ap_lo in mmHg)",
                min_value=40, max_value=160,
                value=int(st.session_state.get("p_ap_lo", 85)),
                step=1,
                help="Lower blood pressure between beats. Clinical ideal: < 80 mmHg."
            )
            st.caption("Lower pressure between cardiac beats (Normal: < 80 mmHg)")

        # Live Dynamic AHA Blood Pressure Classification
        bp_stage, bp_color = classify_blood_pressure(int(ap_hi), int(ap_lo))
        st.markdown(f"""
        <div style="margin: 8px 0 16px 0; display: inline-flex; align-items: center; gap: 8px; background: {bp_color}18; border: 1px solid {bp_color}44; color: {bp_color}; padding: 5px 14px; border-radius: 20px; font-size: 12.5px; font-weight: 700;">
            <span>🩺 AHA Hemodynamic Stage:</span> <span>{bp_stage}</span>
        </div>
        """, unsafe_allow_html=True)

        # Group 4: Laboratory Results
        st.markdown("<div class='form-group-title'><span>🧪</span> Laboratory Chemistry Biomarkers</div>", unsafe_allow_html=True)
        col_lab1, col_lab2 = st.columns(2)
        with col_lab1:
            chol_choice = st.selectbox(
                "Serum Cholesterol Level",
                [
                    (1, "1 - Normal (< 200 mg/dL)"),
                    (2, "2 - Above Normal (200 - 239 mg/dL)"),
                    (3, "3 - Well Above Normal (≥ 240 mg/dL)")
                ],
                format_func=lambda x: x[1],
                index=int(st.session_state.get("p_chol", 1)) - 1
            )[0]
        with col_lab2:
            gluc_choice = st.selectbox(
                "Fasting Glucose Level",
                [
                    (1, "1 - Normal (< 100 mg/dL)"),
                    (2, "2 - Above Normal (100 - 125 mg/dL)"),
                    (3, "3 - Well Above Normal (≥ 126 mg/dL)")
                ],
                format_func=lambda x: x[1],
                index=int(st.session_state.get("p_gluc", 1)) - 1
            )[0]

        # Group 5: Lifestyle Factors
        st.markdown("<div class='form-group-title'><span>🏃</span> Lifestyle & Behavioral Habits</div>", unsafe_allow_html=True)
        col_life1, col_life2, col_life3 = st.columns(3)
        with col_life1:
            preset_smoke = st.session_state.get("p_smoke", "No")
            smoke_label = st.radio("Tobacco Smoker", ["No", "Yes"], horizontal=True, index=1 if preset_smoke == "Yes" else 0)
            smoke_val = 1 if smoke_label == "Yes" else 0
        with col_life2:
            preset_alco = st.session_state.get("p_alco", "No")
            alco_label = st.radio("Alcohol Intake", ["No", "Yes"], horizontal=True, index=1 if preset_alco == "Yes" else 0)
            alco_val = 1 if alco_label == "Yes" else 0
        with col_life3:
            preset_active = st.session_state.get("p_active", "Active")
            active_label = st.radio("Physical Activity", ["Active", "Inactive"], horizontal=True, index=0 if preset_active == "Active" else 1)
            active_val = 1 if active_label == "Active" else 0

        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

        # Form Action Buttons
        btn_c1, btn_c2 = st.columns([1.6, 1.0])
        with btn_c1:
            predict_clicked = st.button("❤️ Predict Heart Disease Risk", type="primary", use_container_width=True, key="btn_main_predict")
        with btn_c2:
            reset_clicked = st.button("🔄 Reset to Default Values", type="secondary", use_container_width=True, key="btn_main_reset")

        if reset_clicked:
            for k in ["p_age", "p_gender", "p_height", "p_weight", "p_ap_hi", "p_ap_lo", "p_chol", "p_gluc", "p_smoke", "p_alco", "p_active", "last_prediction"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()

        # Medical Disclaimer inside form
        render_medical_disclaimer()

    # -------------------------------------------------------------
    # 3. PREDICTION EXECUTION & RESULTS PRESENTATION
    # -------------------------------------------------------------
    if predict_clicked:
        patient_payload = {
            "gender": gender_val,
            "height": float(height),
            "weight": float(weight),
            "ap_hi": int(ap_hi),
            "ap_lo": int(ap_lo),
            "cholesterol": int(chol_choice),
            "gluc": int(gluc_choice),
            "smoke": int(smoke_val),
            "alco": int(alco_val),
            "active": int(active_val),
            "age_years": float(age)
        }

        # Validation audit
        validation_errors = validate_patient_inputs(patient_payload)
        if validation_errors:
            for err in validation_errors:
                st.error(f"Validation Warning: {err}")
        else:
            with st.spinner("Analyzing cardiovascular risk profile with trained ensemble..."):
                res = predict_risk(patient_payload, model_choice=selected_model)
                st.session_state["last_prediction"] = {
                    "result": res,
                    "patient": patient_payload,
                    "bmi": live_bmi
                }

    # Render Results if available in session
    if st.session_state.get("last_prediction"):
        saved = st.session_state["last_prediction"]
        res = saved["result"]
        patient = saved["patient"]
        prob_pct = res["risk_percentage"]
        label = res["risk_label"]
        model_name = res["model_used"]

        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <div class="pro-badge">
                <span class="pro-pulse-dot"></span> EVALUATION COMPLETE
            </div>
            <h3 style="font-size: 28px; font-weight: 800; color: #FFFFFF; margin: 0 0 6px 0; letter-spacing: -0.5px;">
                Cardiovascular Screening Assessment
            </h3>
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            res_col_left, res_col_right = st.columns([1.1, 1.0], gap="large")

            with res_col_left:
                render_result_banner(label, prob_pct, model_name)
                render_risk_gauge(res["risk_probability"])

            with res_col_right:
                st.markdown("<div class='form-group-title' style='margin-top: 0;'><span>🔍</span> Key Factor Breakdown</div>", unsafe_allow_html=True)
                factors = analyze_key_factors(patient, saved["bmi"])
                for f in factors:
                    render_factor_pill(f)

                st.markdown("<div class='form-group-title'><span>💡</span> Clinical Recommendations</div>", unsafe_allow_html=True)
                if "ELEVATED" in label.upper() or "HIGH" in label.upper():
                    st.markdown("""
                    <div style="background: rgba(225, 29, 72, 0.08); border: 1px solid rgba(225, 29, 72, 0.3); border-radius: 12px; padding: 16px; font-size: 13.5px; line-height: 1.65; color: #F1F5F9;">
                        <b style="color: #FB7185;">Actionable Next Steps:</b>
                        <ul style="margin: 8px 0 0 0; padding-left: 20px;">
                            <li><b>Medical Consultation:</b> Schedule a comprehensive clinical exam with a healthcare professional or cardiologist.</li>
                            <li><b>Hemodynamic Monitoring:</b> Track and log systolic/diastolic blood pressure twice daily.</li>
                            <li><b>Dietary Regimen:</b> Follow the DASH eating plan (reduce dietary sodium &lt; 2,000 mg/day).</li>
                            <li><b>Aerobic Exercise:</b> Target 150 minutes of moderate-intensity cardiovascular exercise per week.</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 16px; font-size: 13.5px; line-height: 1.65; color: #F1F5F9;">
                        <b style="color: #34D399;">Preventative Wellness Guidance:</b>
                        <ul style="margin: 8px 0 0 0; padding-left: 20px;">
                            <li><b>Sustain Active Habits:</b> Continue regular aerobic activity (minimum 150 min/wk).</li>
                            <li><b>Nutritional Balance:</b> Prioritize whole foods, fiber, healthy fats, and hydration.</li>
                            <li><b>Routine Screening:</b> Annual blood pressure, fasting lipid, and glucose panels.</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 4. SECTION: WHY CHOOSE CARDIOPREDICT? (6 CARDS GRID)
    # -------------------------------------------------------------
    st.markdown("""
    <div id="features" style="text-align: center; margin-bottom: 40px; scroll-margin-top: 100px;">
        <h2 style="font-size: 34px; font-weight: 800; color: #FFFFFF; margin-bottom: 8px; letter-spacing: -0.8px;">
            Why Choose CardioPredict?
        </h2>
        <p style="font-size: 15.5px; color: #94A3B8; max-width: 620px; margin: 0 auto; line-height: 1.6;">
            Our advanced AI platform delivers accurate, instant, and clinically-informed cardiovascular risk assessments.
        </p>
    </div>
    """, unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        render_feature_card(
            "🧠",
            "Advanced ML Models",
            "Trained and evaluated on ensemble architectures including Random Forest and AdaBoost, fine-tuned across 70,000 patient records."
        )
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
        render_feature_card(
            "🎯",
            "73% Clinical Precision",
            "Validated across 5-fold stratified cross-validation matching published peer benchmarks on standardized clinical examinations."
        )
    with fc2:
        render_feature_card(
            "⚡",
            "Instant Assessment",
            "Real-time sub-10 millisecond in-process risk probability computation with zero external network lag or server latency."
        )
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
        render_feature_card(
            "🔒",
            "Complete Data Privacy",
            "All health metrics remain strictly inside your private session; no personal vitals or patient records are ever logged or stored."
        )
    with fc3:
        render_feature_card(
            "📊",
            "11 Health Factors",
            "Holistic multi-factorial risk profiling incorporating vitals, anthropometry, lipid/glucose biochemistry, and lifestyle habits."
        )
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
        render_feature_card(
            "🎓",
            "Academic Rigor",
            "Built strictly according to Darshan University Computer Engineering ML SOP with dual ensemble training and systematic overfitting audit."
        )

    st.markdown("<div style='height: 64px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 5. SECTION: HOW IT WORKS (3 STEPS FLOW)
    # -------------------------------------------------------------
    st.markdown("""
    <div id="how-it-works" style="text-align: center; margin-bottom: 44px; scroll-margin-top: 100px;">
        <h2 style="font-size: 34px; font-weight: 800; color: #FFFFFF; margin-bottom: 8px; letter-spacing: -0.8px;">
            How It Works
        </h2>
        <p style="font-size: 15.5px; color: #94A3B8; max-width: 600px; margin: 0 auto;">
            Three simple steps to assess your cardiovascular health
        </p>
    </div>
    """, unsafe_allow_html=True)

    hw1, hw2, hw3 = st.columns(3)
    with hw1:
        render_how_it_works_step(
            "01",
            "Enter Your Metrics",
            "Fill in your health details including age, blood pressure, cholesterol, glucose, and lifestyle habits."
        )
    with hw2:
        render_how_it_works_step(
            "02",
            "AI Neural Analysis",
            "Our fine-tuned ensemble machine learning models analyze complex non-linear interactions across your metrics."
        )
    with hw3:
        render_how_it_works_step(
            "03",
            "Get Actionable Insights",
            "Receive an instant risk probability score with clear factor breakdowns and tailored preventative guidance."
        )
