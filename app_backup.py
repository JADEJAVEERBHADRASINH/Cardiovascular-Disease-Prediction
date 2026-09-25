import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CardioLife AI by Veerbhadrasinh",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.html("""
<style>

    /* =========================
       MAIN APPLICATION
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(239, 68, 68, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(14, 165, 233, 0.10),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #07111f 0%,
                #0b1728 50%,
                #101d31 100%
            );
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #050b14 0%,
                #091426 55%,
                #0d1b30 100%
            );

        border-right: 1px solid rgba(255,255,255,0.08);
    }


    /* =========================
       SIDEBAR BRAND
       ========================= */

    .brand-box {
        text-align: center;
        padding: 25px 10px 30px 10px;
    }

    .brand-icon {
        width: 70px;
        height: 70px;
        margin: auto;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 20px;

        background:
            linear-gradient(
                135deg,
                #ef4444,
                #dc2626
            );

        box-shadow:
            0 0 30px rgba(239,68,68,0.35);

        font-size: 35px;
    }

    .brand-name {
        margin-top: 14px;

        font-size: 25px;
        font-weight: 800;

        color: #ffffff;
    }

    .brand-subtitle {
        margin-top: 5px;

        font-size: 10px;

        letter-spacing: 2px;

        color: #94a3b8;
    }


    /* =========================
       TOP STATUS
       ========================= */

    .status-box {
        display: flex;

        justify-content: space-between;
        align-items: center;

        padding: 13px 18px;

        margin-bottom: 25px;

        border-radius: 14px;

        background: rgba(255,255,255,0.04);

        border: 1px solid rgba(255,255,255,0.08);
    }

    .status-text {
        color: #94a3b8;

        font-size: 13px;
    }

    .online {
        color: #4ade80;

        font-size: 13px;

        font-weight: 600;
    }

    .online-dot {
        display: inline-block;

        width: 8px;
        height: 8px;

        margin-right: 7px;

        border-radius: 50%;

        background: #22c55e;

        box-shadow:
            0 0 10px #22c55e;
    }


    /* =========================
       HERO
       ========================= */

    .hero-box {
        padding: 38px;

        border-radius: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(239,68,68,0.14),
                rgba(14,165,233,0.08)
            );

        border:
            1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 20px 60px rgba(0,0,0,0.25);

        margin-bottom: 30px;
    }

    .hero-tag {
        display: inline-block;

        padding: 7px 13px;

        border-radius: 20px;

        background:
            rgba(239,68,68,0.14);

        color: #f87171;

        font-size: 10px;

        font-weight: 700;

        letter-spacing: 1.5px;
    }

    .hero-title {
        margin-top: 17px;

        font-size: 42px;

        line-height: 1.12;

        font-weight: 800;

        color: #ffffff;
    }

    .hero-highlight {
        color: #f87171;
    }

    .hero-description {
        max-width: 720px;

        margin-top: 15px;

        color: #94a3b8;

        font-size: 15px;

        line-height: 1.7;
    }


    /* =========================
       SECTION TITLE
       ========================= */

    .section-title {
        margin-top: 28px;
        margin-bottom: 15px;

        color: #ffffff;

        font-size: 23px;

        font-weight: 700;
    }


    /* =========================
       CARDS
       ========================= */

    .info-card {
        min-height: 155px;

        padding: 24px;

        border-radius: 18px;

        background:
            rgba(255,255,255,0.045);

        border:
            1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 12px 35px rgba(0,0,0,0.18);
    }

    .info-icon {
        font-size: 30px;

        margin-bottom: 10px;
    }

    .info-title {
        color: #ffffff;

        font-size: 17px;

        font-weight: 700;
    }

    .info-text {
        margin-top: 8px;

        color: #94a3b8;

        font-size: 13px;

        line-height: 1.6;
    }


    /* =========================
       FORM CONTAINER
       ========================= */

    .form-header {
        padding: 20px 22px;

        margin-bottom: 10px;

        border-radius: 15px;

        background:
            rgba(255,255,255,0.04);

        border:
            1px solid rgba(255,255,255,0.08);
    }

    .form-header-title {
        color: #ffffff;

        font-size: 19px;

        font-weight: 700;
    }

    .form-header-text {
        margin-top: 5px;

        color: #94a3b8;

        font-size: 13px;
    }


    /* =========================
       BMI
       ========================= */

    .bmi-box {
        display: flex;

        align-items: center;

        justify-content: space-between;

        padding: 16px 20px;

        margin-top: 12px;
        margin-bottom: 20px;

        border-radius: 13px;

        background:
            rgba(14,165,233,0.08);

        border:
            1px solid rgba(14,165,233,0.20);
    }

    .bmi-label {
        color: #94a3b8;

        font-size: 13px;
    }

    .bmi-value {
        color: #67e8f9;

        font-size: 25px;

        font-weight: 800;
    }


    /* =========================
       RESULT
       ========================= */

    .result-box {
        padding: 35px;

        margin-top: 20px;

        text-align: center;

        border-radius: 22px;

        background:
            linear-gradient(
                135deg,
                rgba(239,68,68,0.10),
                rgba(14,165,233,0.08)
            );

        border:
            1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 15px 45px rgba(0,0,0,0.20);
    }

    .result-icon {
        font-size: 55px;
    }

    .result-title {
        margin-top: 10px;

        color: #ffffff;

        font-size: 27px;

        font-weight: 800;
    }

    .result-text {
        margin-top: 8px;

        color: #94a3b8;

        font-size: 14px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        padding-top: 50px;
        padding-bottom: 20px;

        text-align: center;

        color: #64748b;

        font-size: 12px;
    }


    /* =========================
       STREAMLIT INPUTS
       ========================= */

    div[data-baseweb="input"] {
        background: #111c2d !important;

        border-radius: 10px !important;

        border: 1px solid #26364d !important;
    }

    div[data-baseweb="select"] > div {
        background: #111c2d !important;

        border-radius: 10px !important;

        border: 1px solid #26364d !important;
    }

    label {
        color: #cbd5e1 !important;
    }


    /* =========================
       BUTTON
       ========================= */

    .stButton > button,
    .stFormSubmitButton > button {

        border: none !important;

        border-radius: 11px !important;

        min-height: 48px;

        color: white !important;

        font-weight: 700 !important;

        background:
            linear-gradient(
                135deg,
                #ef4444,
                #dc2626
            ) !important;

        box-shadow:
            0 10px 25px rgba(239,68,68,0.25);

        transition: 0.2s;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 15px 35px rgba(239,68,68,0.40);
    }


    /* =========================
       HIDE STREAMLIT FOOTER
       ========================= */

    footer {
        visibility: hidden;
    }

</style>
""")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.html("""
<div class="brand-box">

    <div class="brand-icon">
        🫀
    </div>

    <div class="brand-name">
        CardioLife
    </div>

    <div class="brand-subtitle">
        CLINICAL AI PLATFORM
    </div>

</div>
""")


page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🩺 Risk Diagnostics",
        "💡 Health Guidance",
        "ℹ️ About"
    ]
)


st.sidebar.markdown("---")


st.sidebar.html("""
<div style="
    padding:16px;
    border-radius:14px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.06);
">

    <div style="
        color:#64748b;
        font-size:10px;
        letter-spacing:1.5px;
    ">
        SYSTEM STATUS
    </div>

    <div style="
        color:#4ade80;
        font-size:13px;
        font-weight:600;
        margin-top:10px;
    ">
        ● Frontend Online
    </div>

</div>
""")


# =========================================================
# STATUS BAR
# =========================================================

st.html("""
<div class="status-box">

    <div class="status-text">
        CardioLife / Clinical Intelligence
    </div>

    <div class="online">
        <span class="online-dot"></span>
        System Online
    </div>

</div>
""")


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.html("""
    <div class="hero-box">

        <span class="hero-tag">
            AI POWERED CARDIOVASCULAR ANALYSIS
        </span>

        <div class="hero-title">
            Intelligent Heart Health
            <br>
            <span class="hero-highlight">
                Risk Assessment
            </span>
        </div>

        <div class="hero-description">
            CardioLife is a machine-learning based cardiovascular
            disease prediction system. Enter patient health
            information and use the trained model to assess
            cardiovascular disease risk.
        </div>

    </div>
    """)


    st.html("""
    <div class="section-title">
        Platform Capabilities
    </div>
    """)


    col1, col2, col3 = st.columns(3)


    with col1:
        st.html("""
        <div class="info-card">

            <div class="info-icon">🤖</div>

            <div class="info-title">
                Machine Learning
            </div>

            <div class="info-text">
                Uses your trained machine learning model
                to analyze cardiovascular health factors.
            </div>

        </div>
        """)


    with col2:
        st.html("""
        <div class="info-card">

            <div class="info-icon">⚡</div>

            <div class="info-title">
                Fast Assessment
            </div>

            <div class="info-text">
                Patient information can be submitted
                quickly through the interactive interface.
            </div>

        </div>
        """)


    with col3:
        st.html("""
        <div class="info-card">

            <div class="info-icon">🩺</div>

            <div class="info-title">
                Clinical Factors
            </div>

            <div class="info-text">
                Analyze blood pressure, cholesterol,
                glucose, BMI and lifestyle information.
            </div>

        </div>
        """)


    st.html("""
    <div class="section-title">
        How It Works
    </div>
    """)


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.html("""
        <div class="info-card" style="text-align:center;">
            <div class="info-icon">👤</div>
            <div class="info-title">1. Enter Data</div>
            <div class="info-text">
                Enter patient information.
            </div>
        </div>
        """)


    with col2:
        st.html("""
        <div class="info-card" style="text-align:center;">
            <div class="info-icon">📤</div>
            <div class="info-title">2. Submit</div>
            <div class="info-text">
                Send the information for analysis.
            </div>
        </div>
        """)


    with col3:
        st.html("""
        <div class="info-card" style="text-align:center;">
            <div class="info-icon">🤖</div>
            <div class="info-title">3. Predict</div>
            <div class="info-text">
                ML model analyzes the input.
            </div>
        </div>
        """)


    with col4:
        st.html("""
        <div class="info-card" style="text-align:center;">
            <div class="info-icon">📊</div>
            <div class="info-title">4. Result</div>
            <div class="info-text">
                Prediction is displayed.
            </div>
        </div>
        """)


# =========================================================
# RISK DIAGNOSTICS
# =========================================================

elif page == "🩺 Risk Diagnostics":

    st.html("""
    <div class="hero-box">

        <span class="hero-tag">
            CLINICAL ASSESSMENT
        </span>

        <div class="hero-title">
            Cardiovascular Risk
            <br>
            <span class="hero-highlight">
                Diagnostics
            </span>
        </div>

        <div class="hero-description">
            Enter the patient's cardiovascular health
            information below. The data will later be
            sent to the FastAPI backend for prediction.
        </div>

    </div>
    """)


    # -----------------------------------------------------
    # PATIENT INFORMATION
    # -----------------------------------------------------

    st.html("""
    <div class="form-header">

        <div class="form-header-title">
            👤 Patient Information
        </div>

        <div class="form-header-text">
            Basic physical information about the patient.
        </div>

    </div>
    """)


    col1, col2, col3 = st.columns(3)


    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=50
        )


    with col2:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )


    with col3:

        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=170.0
        )


    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=300.0,
        value=70.0
    )


    # BMI calculation

    bmi = weight / ((height / 100) ** 2)


    st.html(f"""
    <div class="bmi-box">

        <div class="bmi-label">
            Calculated Body Mass Index (BMI)
        </div>

        <div class="bmi-value">
            {bmi:.2f}
        </div>

    </div>
    """)


    # -----------------------------------------------------
    # CLINICAL VITALS
    # -----------------------------------------------------

    st.html("""
    <div class="form-header">

        <div class="form-header-title">
            ❤️ Clinical Vitals
        </div>

        <div class="form-header-text">
            Enter blood pressure and laboratory information.
        </div>

    </div>
    """)


    col1, col2 = st.columns(2)


    with col1:

        ap_hi = st.number_input(
            "Systolic Blood Pressure",
            min_value=50,
            max_value=300,
            value=120
        )


    with col2:

        ap_lo = st.number_input(
            "Diastolic Blood Pressure",
            min_value=30,
            max_value=200,
            value=80
        )


    col1, col2 = st.columns(2)


    with col1:

        cholesterol = st.selectbox(
            "Cholesterol",
            [
                "Normal",
                "Above Normal",
                "High"
            ]
        )


    with col2:

        gluc = st.selectbox(
            "Glucose",
            [
                "Normal",
                "Above Normal",
                "High"
            ]
        )


    # -----------------------------------------------------
    # LIFESTYLE
    # -----------------------------------------------------

    st.html("""
    <div class="form-header">

        <div class="form-header-title">
            🏃 Lifestyle
        </div>

        <div class="form-header-text">
            Select the patient's lifestyle characteristics.
        </div>

    </div>
    """)


    col1, col2, col3 = st.columns(3)


    with col1:

        smoke = st.checkbox(
            "🚬 Smoker"
        )


    with col2:

        alco = st.checkbox(
            "🍺 Alcohol Consumer"
        )


    with col3:

        active = st.checkbox(
            "🏃 Physically Active"
        )


    st.write("")


    # -----------------------------------------------------
    # PREDICT BUTTON
    # -----------------------------------------------------

    predict = st.button(
        "🔍 RUN CARDIOVASCULAR RISK ANALYSIS",
        use_container_width=True
    )


    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    if predict:

        st.html("""
        <div class="result-box">

            <div class="result-icon">
                🧠
            </div>

            <div class="result-title">
                Ready for Analysis
            </div>

            <div class="result-text">
                Patient information has been collected successfully.
            </div>

        </div>
        """)

        st.info(
            "FastAPI connection will be added next. "
            "The prediction button will then send this "
            "patient information to your ML backend."
        )


# =========================================================
# HEALTH GUIDANCE
# =========================================================

elif page == "💡 Health Guidance":

    st.html("""
    <div class="hero-box">

        <span class="hero-tag">
            HEART HEALTH
        </span>

        <div class="hero-title">
            Clinical Health
            <br>
            <span class="hero-highlight">
                Guidance
            </span>
        </div>

        <div class="hero-description">
            General lifestyle information related to
            cardiovascular health.
        </div>

    </div>
    """)


    col1, col2 = st.columns(2)


    with col1:

        st.html("""
        <div class="info-card">

            <div class="info-icon">🥗</div>

            <div class="info-title">
                Healthy Nutrition
            </div>

            <div class="info-text">
                Eat a balanced diet containing fruits,
                vegetables and nutritious foods.
                Reduce excessive salt and highly
                processed foods.
            </div>

        </div>
        """)


    with col2:

        st.html("""
        <div class="info-card">

            <div class="info-icon">🏃</div>

            <div class="info-title">
                Physical Activity
            </div>

            <div class="info-text">
                Maintain regular physical activity
                and avoid prolonged periods of inactivity.
            </div>

        </div>
        """)


    st.write("")


    col1, col2 = st.columns(2)


    with col1:

        st.html("""
        <div class="info-card">

            <div class="info-icon">🚭</div>

            <div class="info-title">
                Avoid Smoking
            </div>

            <div class="info-text">
                Avoiding tobacco is an important part
                of maintaining cardiovascular health.
            </div>

        </div>
        """)


    with col2:

        st.html("""
        <div class="info-card">

            <div class="info-icon">😴</div>

            <div class="info-title">
                Sleep & Stress
            </div>

            <div class="info-text">
                Maintain healthy sleep habits and
                manage everyday stress.
            </div>

        </div>
        """)


    st.warning(
        "⚠️ This application is an academic machine-learning "
        "project and should not be used as a replacement "
        "for professional medical advice."
    )


# =========================================================
# ABOUT
# =========================================================

elif page == "ℹ️ About":

    st.html("""
    <div class="hero-box">

        <span class="hero-tag">
            PROJECT INFORMATION
        </span>

        <div class="hero-title">
            About
            <br>
            <span class="hero-highlight">
                CardioLife AI
            </span>
        </div>

        <div class="hero-description">
            A machine-learning based cardiovascular disease
            prediction project developed for academic purposes.
        </div>

    </div>
    """)


    col1, col2, col3 = st.columns(3)


    with col1:

        st.html("""
        <div class="info-card">

            <div class="info-icon">🎨</div>

            <div class="info-title">
                Frontend
            </div>

            <div class="info-text">
                Streamlit interactive web interface.
            </div>

        </div>
        """)


    with col2:

        st.html("""
        <div class="info-card">

            <div class="info-icon">⚡</div>

            <div class="info-title">
                Backend
            </div>

            <div class="info-text">
                FastAPI REST backend.
            </div>

        </div>
        """)


    with col3:

        st.html("""
        <div class="info-card">

            <div class="info-icon">🤖</div>

            <div class="info-title">
                Machine Learning
            </div>

            <div class="info-text">
                Cardiovascular disease classification model.
            </div>

        </div>
        """)


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    🫀 <b>CardioLife AI</b>
    &nbsp; • &nbsp;
    Cardiovascular Disease Prediction By Veerbhadrasinh 

    <br><br>

    Machine Learning Project

</div>
""")