"""
CardioPredict Pro Design System.
World-class UI/UX aesthetic matching high-end modern applications (Linear, Vercel, Shadcn, Supabase).
Features:
- Deep luxury dark canvas with subtle radial illumination (#060911, #090D16, #0F172A)
- Glassmorphic backdrop blur & ultra-fine 1px border lighting
- Vibrant pulse-glow crimson heart accent (#E11D48, #F43F5E)
- Custom segmented control radios & elevated number inputs
- Refined typography with Plus Jakarta Sans & Inter
- Polished medical-grade visualization containers and result scorecards
"""
import streamlit as st

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* =========================================================
       1. GLOBAL RESET & PRO DARK CANVAS
       ========================================================= */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #070A12 !important;
        background-image: 
            radial-gradient(circle at 50% 0%, rgba(225, 29, 72, 0.15) 0%, transparent 60%),
            radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px) !important;
        background-size: 100% 100%, 28px 28px !important;
        background-attachment: fixed !important;
        color: #F8FAFC !important;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }

    /* Container Spacing */
    .main .block-container {
        max-width: 1240px !important;
        padding-top: 1.25rem !important;
        padding-bottom: 5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        margin: 0 auto !important;
    }

    /* Streamlit controls cleanup */
    section[data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    button[data-testid="baseButton-header"],
    header[data-testid="stHeader"] {
        display: none !important;
    }
    footer { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; }

    /* Custom Modern Scrollbar */
    ::-webkit-scrollbar {
        width: 7px;
        height: 7px;
    }
    ::-webkit-scrollbar-track {
        background: #070A12;
    }
    ::-webkit-scrollbar-thumb {
        background: #1E293B;
        border-radius: 999px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #334155;
    }

    /* =========================================================
       2. HERO SECTION & AMBIENT ILLUMINATION
       ========================================================= */
    .hero-glow-bg {
        position: relative;
        overflow: hidden;
        padding: 30px 0 10px 0;
    }
    .hero-glow-blob {
        position: absolute;
        top: 10%;
        left: 50%;
        transform: translateX(-50%);
        width: 820px;
        height: 380px;
        background: radial-gradient(circle, rgba(225, 29, 72, 0.24) 0%, rgba(225, 29, 72, 0.06) 50%, rgba(7, 10, 18, 0) 75%);
        filter: blur(90px);
        pointer-events: none;
        z-index: 0;
    }

    /* Pro Pulsing Badge */
    .pro-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 18px;
        border-radius: 9999px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #E2E8F0;
        font-size: 12.5px;
        font-weight: 600;
        letter-spacing: 0.6px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        margin-bottom: 22px;
    }
    .pro-pulse-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #E11D48;
        box-shadow: 0 0 10px #E11D48;
        display: inline-block;
        animation: pulse-glow 2s infinite ease-in-out;
    }
    @keyframes pulse-glow {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.45; transform: scale(1.15); }
    }

    /* Hero Headings */
    .hero-heading {
        font-size: 56px;
        font-weight: 800;
        letter-spacing: -1.8px;
        line-height: 1.12;
        color: #FFFFFF;
        margin: 0 auto 20px auto;
        max-width: 860px;
        text-align: center;
    }
    .hero-heading-highlight {
        color: #E11D48;
        background: linear-gradient(135deg, #F43F5E 0%, #E11D48 50%, #BE123C 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px rgba(225, 29, 72, 0.35);
    }
    .hero-description {
        font-size: 17.5px;
        line-height: 1.7;
        color: #94A3B8;
        max-width: 660px;
        margin: 0 auto 34px auto;
        text-align: center;
        font-weight: 400;
    }

    /* Floating Trust Badges */
    .trust-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 13.5px;
        color: #CBD5E1;
        font-weight: 500;
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.06);
        padding: 6px 14px;
        border-radius: 999px;
        backdrop-filter: blur(8px);
    }

    /* =========================================================
       3. PRO CARD SYSTEM & GLASSMORPHISM
       ========================================================= */
    .vercel-card, 
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.85) 0%, rgba(10, 15, 29, 0.95) 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 18px !important;
        padding: 26px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(16px) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .vercel-card:hover, 
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(225, 29, 72, 0.35) !important;
        box-shadow: 0 14px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(225, 29, 72, 0.15) !important;
    }

    /* 4-Stat Metric Card */
    .stat-counter-card {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.7) 0%, rgba(10, 15, 28, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 22px 18px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
        position: relative;
        overflow: hidden;
    }
    .stat-counter-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 20%;
        right: 20%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(225, 29, 72, 0.6), transparent);
    }
    .stat-counter-card:hover {
        transform: translateY(-3px);
        border-color: rgba(225, 29, 72, 0.3);
    }
    .stat-counter-num {
        font-size: 40px;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.1;
        letter-spacing: -1px;
        margin-bottom: 4px;
        background: linear-gradient(135deg, #FFFFFF 30%, #FDA4AF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stat-counter-label {
        font-size: 13.5px;
        color: #94A3B8;
        font-weight: 600;
        letter-spacing: 0.2px;
    }

    /* Feature Card */
    .vercel-card-icon-box {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        background: rgba(225, 29, 72, 0.12);
        border: 1px solid rgba(225, 29, 72, 0.25);
        color: #F43F5E;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 14px rgba(225, 29, 72, 0.2);
    }
    .vercel-card-title {
        font-size: 18px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 8px;
        letter-spacing: -0.3px;
    }
    .vercel-card-desc {
        font-size: 13.5px;
        color: #94A3B8;
        line-height: 1.65;
        margin: 0;
    }

    /* Section Headers */
    .form-group-title {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 15.5px;
        font-weight: 700;
        color: #FFFFFF;
        padding-bottom: 10px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin: 24px 0 16px 0;
        letter-spacing: -0.2px;
    }

    /* Step Circles (01, 02, 03) */
    .step-circle-outer {
        position: relative;
        width: 84px;
        height: 84px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(225, 29, 72, 0.16) 0%, rgba(15, 23, 42, 0.6) 70%);
        border: 1px solid rgba(225, 29, 72, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 22px auto;
        box-shadow: 0 0 24px rgba(225, 29, 72, 0.2);
    }
    .step-circle-badge {
        position: absolute;
        top: -4px;
        right: -4px;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%);
        color: white;
        font-size: 12px;
        font-weight: 800;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 8px rgba(225, 29, 72, 0.5);
    }

    /* =========================================================
       4. PRO FORM CONTROLS & WIDGET OVERRIDES
       ========================================================= */
    /* Input Box & Number Inputs */
    div[data-baseweb="input"],
    div[data-baseweb="input"] > div,
    div[data-baseweb="input"] input,
    div[data-testid="stNumberInput"] input,
    input[data-testid="stNumberInputField"] {
        background-color: #090D16 !important;
        background: #090D16 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border-color: rgba(255, 255, 255, 0.12) !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #E11D48 !important;
        box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.25) !important;
        background-color: #0B0F1B !important;
    }

    /* Stepper Buttons (+ and -) */
    div[data-testid="stNumberInput"] button {
        background-color: #0F172A !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
    }
    div[data-testid="stNumberInput"] button:hover {
        background-color: #1E293B !important;
        color: #E11D48 !important;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background: #090D16 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 10px !important;
        color: #FFFFFF !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    div[data-baseweb="select"] > div:focus-within {
        border-color: #E11D48 !important;
        box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.25) !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #0F172A !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6) !important;
    }
    li[data-baseweb="menu-item"] {
        color: #F8FAFC !important;
        font-size: 13.5px !important;
        padding: 10px 14px !important;
    }
    li[data-baseweb="menu-item"]:hover {
        background-color: rgba(225, 29, 72, 0.18) !important;
        color: #FFFFFF !important;
    }

    /* Widget Labels */
    label[data-testid="stWidgetLabel"] p {
        color: #E2E8F0 !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        letter-spacing: 0.1px !important;
        margin-bottom: 4px !important;
    }
    div[data-testid="stCaptionContainer"] p {
        color: #64748B !important;
        font-size: 12px !important;
    }

    /* Segmented Control Radio Buttons */
    .stRadio div[role="radiogroup"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        background: #090D16 !important;
        padding: 5px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        gap: 8px !important;
        align-items: center !important;
    }
    .stRadio div[role="radiogroup"] label {
        flex: 1 1 0% !important;
        white-space: nowrap !important;
        min-width: 0 !important;
        background: transparent !important;
        padding: 7px 12px !important;
        border-radius: 7px !important;
        border: 1px solid transparent !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
    }
    .stRadio div[role="radiogroup"] label:hover {
        background: rgba(255, 255, 255, 0.05) !important;
    }
    .stRadio div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {
        color: #CBD5E1 !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        white-space: nowrap !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .stRadio div[role="radiogroup"] label:has(input:checked) {
        background: rgba(225, 29, 72, 0.2) !important;
        border: 1px solid rgba(225, 29, 72, 0.5) !important;
        box-shadow: 0 0 12px rgba(225, 29, 72, 0.25) !important;
    }
    .stRadio div[role="radiogroup"] label:has(input:checked) div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
    /* Hide the radio circle dot inside segmented pills */
    .stRadio div[role="radiogroup"] label > div:first-child {
        display: none !important;
    }

    /* =========================================================
       5. PRO BUTTONS & CALLS TO ACTION
       ========================================================= */
    /* Primary Crimson Button */
    button[data-testid="baseButton-primary"], 
    div.stFormSubmitButton > button,
    button[kind="primary"] {
        background: linear-gradient(135deg, #F43F5E 0%, #E11D48 60%, #BE123C 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        letter-spacing: 0.3px !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        min-height: 48px !important;
        box-shadow: 0 4px 20px rgba(225, 29, 72, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.25) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    button[data-testid="baseButton-primary"]:hover, 
    div.stFormSubmitButton > button:hover,
    button[kind="primary"]:hover {
        background: linear-gradient(135deg, #FB7185 0%, #F43F5E 60%, #E11D48 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(225, 29, 72, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.35) !important;
    }
    button[data-testid="baseButton-primary"]:active {
        transform: translateY(0px) !important;
    }

    /* Secondary Buttons */
    button[data-testid="baseButton-secondary"],
    button[kind="secondary"] {
        background: #090D16 !important;
        color: #E2E8F0 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        padding: 11px 22px !important;
        min-height: 46px !important;
        transition: all 0.2s ease !important;
    }
    button[data-testid="baseButton-secondary"]:hover,
    button[kind="secondary"]:hover {
        background: #1E293B !important;
        color: #FFFFFF !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-1px) !important;
    }

    /* Medical Notice Box */
    .medical-notice-box {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px 20px;
        display: flex;
        gap: 14px;
        align-items: flex-start;
        margin-top: 24px;
        backdrop-filter: blur(8px);
    }
    .medical-notice-box p {
        font-size: 12.5px;
        color: #94A3B8;
        line-height: 1.6;
        margin: 0;
    }

    /* Streamlit Metric Dark Theme Fix */
    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetricDelta"] {
        color: #E11D48 !important;
    }

    /* Tabs Dark Theme */
    button[data-baseweb="tab"] {
        color: #94A3B8 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 12px 20px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;
        border-bottom: 2px solid #E11D48 !important;
    }

    /* =========================================================
       6. PRO FLOATING ISLAND NAVBAR
       ========================================================= */
    html {
        scroll-behavior: smooth !important;
    }

    [id] {
        scroll-margin-top: 100px !important;
    }

    .pro-navbar-wrapper {
        position: sticky;
        top: 8px;
        z-index: 9999;
        margin-bottom: 28px;
        width: 100%;
    }

    .pro-navbar-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(10, 15, 29, 0.88);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 100px;
        padding: 7px 20px;
        box-shadow: 0 10px 36px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }

    .pro-nav-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none !important;
    }

    .pro-brand-icon {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        background: linear-gradient(135deg, #F43F5E 0%, #E11D48 60%, #BE123C 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
        box-shadow: 0 0 16px rgba(225, 29, 72, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }

    .pro-brand-name {
        font-size: 20px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.6px;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .pro-brand-name span {
        color: #F43F5E;
    }

    .pro-brand-tag {
        font-size: 9.5px;
        font-weight: 800;
        background: rgba(225, 29, 72, 0.18);
        border: 1px solid rgba(225, 29, 72, 0.35);
        color: #FDA4AF;
        padding: 2px 7px;
        border-radius: 6px;
        letter-spacing: 0.5px;
    }

    .pro-nav-links {
        display: flex;
        align-items: center;
        gap: 4px;
    }

    .pro-nav-item {
        font-size: 13.5px;
        font-weight: 500;
        color: #94A3B8 !important;
        text-decoration: none !important;
        padding: 7px 13px;
        border-radius: 100px;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid transparent;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    .pro-nav-item:hover {
        color: #FFFFFF !important;
        background: rgba(255, 255, 255, 0.08);
    }

    .pro-nav-item.active {
        color: #FFFFFF !important;
        background: rgba(225, 29, 72, 0.18) !important;
        border-color: rgba(225, 29, 72, 0.45) !important;
        font-weight: 700 !important;
        box-shadow: 0 0 14px rgba(225, 29, 72, 0.25) !important;
    }

    .pro-nav-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .pro-nav-status {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        font-size: 11.5px;
        font-weight: 600;
        color: #34D399;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.25);
        padding: 6px 12px;
        border-radius: 999px;
    }

    .pro-nav-cta-btn {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        background: linear-gradient(135deg, #F43F5E 0%, #E11D48 60%, #BE123C 100%) !important;
        color: #FFFFFF !important;
        text-decoration: none !important;
        font-size: 13px;
        font-weight: 700;
        padding: 8px 18px;
        border-radius: 100px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 2px 12px rgba(225, 29, 72, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.25);
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .pro-nav-cta-btn:hover {
        background: linear-gradient(135deg, #FB7185 0%, #F43F5E 60%, #E11D48 100%) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 20px rgba(225, 29, 72, 0.6);
        color: #FFFFFF !important;
    }

    @media (max-width: 960px) {
        .pro-nav-links {
            display: none !important;
        }
        .pro-nav-status {
            display: none !important;
        }
        .pro-navbar-container {
            padding: 8px 16px !important;
        }
    }
</style>
"""

def inject_theme():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
