"""
CardioPredict Floating Island Navbar.
Pro-grade navigation bar featuring:
- Brand identity with glowing heart icon and 'AI 2.0' badge
- Smooth anchor jump navigation ('Predict', 'Features', 'How It Works')
- Multi-page query parameter routing ('Analytics', 'Model Evaluation', 'Clinical Guidance', 'About')
- Real-time dual ensemble status indicator
- Floating glassmorphic CTA button ('Start Assessment')
"""
import streamlit as st

def render_navbar() -> str:
    """Renders the pro-grade floating island navbar and returns the active page."""
    # Synchronize with query parameters if present in URL
    qp = st.query_params.get("page", None)
    if qp:
        qp_norm = qp.strip().lower()
        if qp_norm in ("analytics", "eda"):
            st.session_state["page"] = "Analytics"
        elif qp_norm in ("evaluation", "model evaluation", "models"):
            st.session_state["page"] = "Model Evaluation"
        elif qp_norm in ("guidance", "clinical guidance", "health"):
            st.session_state["page"] = "Clinical Guidance"
        elif qp_norm in ("about", "about project", "team"):
            st.session_state["page"] = "About Project"
        elif qp_norm in ("assess", "assess risk", "predict", "overview", "home"):
            st.session_state["page"] = "Assess Risk"

    if "page" not in st.session_state:
        st.session_state["page"] = "Assess Risk"

    current = st.session_state["page"]
    is_home = (current in ("Assess Risk", "Overview", "Risk Prediction"))

    # Determine links and active classes
    predict_href = "#assessment-form" if is_home else "?page=Assess+Risk#assessment-form"
    features_href = "#features" if is_home else "?page=Assess+Risk#features"
    how_href = "#how-it-works" if is_home else "?page=Assess+Risk#how-it-works"
    cta_href = "#assessment-form" if is_home else "?page=Assess+Risk#assessment-form"

    predict_active = "active" if is_home else ""
    analytics_active = "active" if current == "Analytics" else ""
    eval_active = "active" if current in ("Model Evaluation", "Evaluation") else ""
    guidance_active = "active" if current in ("Clinical Guidance", "Guidance") else ""
    about_active = "active" if current in ("About Project", "About") else ""

    # Zero-indentation HTML block to prevent CommonMark from treating 4 spaces as <pre><code>
    navbar_html = f"""<header class="pro-navbar-wrapper">
<div class="pro-navbar-container">
<a href="?page=Assess+Risk" target="_self" class="pro-nav-brand">
<div class="pro-brand-icon">❤️</div>
<div style="display: flex; align-items: baseline; gap: 8px;">
<span class="pro-brand-name">Cardio<span>Predict</span></span>
<span class="pro-brand-tag">AI 2.0</span>
</div>
</a>
<nav class="pro-nav-links">
<a href="{predict_href}" target="_self" class="pro-nav-item {predict_active}">Predict</a>
<a href="{features_href}" target="_self" class="pro-nav-item">Features</a>
<a href="{how_href}" target="_self" class="pro-nav-item">How It Works</a>
<a href="?page=Analytics" target="_self" class="pro-nav-item {analytics_active}">Analytics</a>
<a href="?page=Model+Evaluation" target="_self" class="pro-nav-item {eval_active}">Evaluation</a>
<a href="?page=Clinical+Guidance" target="_self" class="pro-nav-item {guidance_active}">Guidance</a>
<a href="?page=About+Project" target="_self" class="pro-nav-item {about_active}">About</a>
</nav>
<div class="pro-nav-actions">
<div class="pro-nav-status">
<span style="width: 7px; height: 7px; border-radius: 50%; background: #10B981; box-shadow: 0 0 8px #10B981; display: inline-block;"></span>
<span>Dual AI Online</span>
</div>
<a href="{cta_href}" target="_self" class="pro-nav-cta-btn">
<span>Start Assessment</span>
<span style="font-size: 15px; font-weight: 800;">&rarr;</span>
</a>
</div>
</div>
</header>"""

    st.markdown(navbar_html, unsafe_allow_html=True)
    return current
