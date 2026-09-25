"""
Sidebar navigation matching CardioPredict reference.
"""
import streamlit as st
from services.predictor import check_backend_health

PAGES = [
    "🏠 Overview",
    "🩺 Predict",
    "📊 Analytics",
    "🔬 Model Insights",
    "📈 Evaluation",
    "💡 Health Guidance",
    "ℹ️ About"
]

def render_sidebar() -> str:
    """Renders custom sidebar matching reference."""
    with st.sidebar:
        st.markdown("""
        <div style="padding: 18px 14px 14px 14px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="
                    width: 38px;
                    height: 38px;
                    border-radius: 10px;
                    background: rgba(20, 184, 166, 0.12);
                    border: 1px solid rgba(20, 184, 166, 0.3);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 20px;
                ">🫀</div>
                <div>
                    <div style="font-size: 18px; font-weight: 700; color: #F8FAFC; letter-spacing: -0.5px;">CardioPredict</div>
                    <div style="font-size: 10px; color: #94A3B8; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600;">AI Screening</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        selected_page = st.radio(
            "Navigation",
            PAGES,
            label_visibility="collapsed"
        )

        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

        # Telemetry Pill
        is_api_live, status_desc = check_backend_health()
        dot_color = "#10B981" if is_api_live else "#38BDF8"

        st.markdown(f"""
        <div style="
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 12px 14px;
        ">
            <div style="font-size: 10px; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 1px;">
                System Status
            </div>
            <div style="display: flex; align-items: center; gap: 8px; margin-top: 6px; font-size: 12px; font-weight: 600; color: #F8FAFC;">
                <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:{dot_color}; box-shadow:0 0 8px {dot_color};"></span>
                {status_desc}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            text-align: center;
            padding-top: 36px;
            font-size: 11px;
            color: #64748B;
        ">
            &copy; 2026 CardioPredict &bull; ML Project
        </div>
        """, unsafe_allow_html=True)

        return selected_page
