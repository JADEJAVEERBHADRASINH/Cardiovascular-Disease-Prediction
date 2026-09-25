"""
Disclaimer Page for CardioML
Compliance with Darshan University SOP and Medical AI Ethics standards.
"""
import streamlit as st

def render():
    st.markdown("""
    <div style="max-width: 820px; margin: 0 auto;">
        <div class="sop-badge" style="margin-bottom: 12px;">
            ⚖️ Academic Compliance & Clinical Ethics
        </div>
        <h2 style="font-size: 32px; font-weight: 800; color: #0F172A; margin: 0 0 12px 0;">
            Institutional Disclaimer & Guidelines
        </h2>
        <p style="font-size: 14px; color: #64748B; margin-bottom: 28px;">
            Darshan University &bull; Computer Engineering Department &bull; Academic Year 2025–26
        </p>

        <div style="
            background: #FEF2F2;
            border: 1px solid #FCA5A5;
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 24px;
        ">
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="font-size: 24px;">🚨</div>
                <div>
                    <div style="font-size: 15px; font-weight: 800; color: #991B1B; margin-bottom: 4px;">
                        Emergency Medical Notice
                    </div>
                    <div style="font-size: 13px; color: #7F1D1D; line-height: 1.6;">
                        If you or someone around you is experiencing acute chest pain, radiating pressure to the arm or jaw, severe shortness of breath, sudden numbness, or loss of consciousness, please call emergency services immediately:
                        <br>
                        <b>National Emergency Hotline: 112 / 108 (India) or 911 (International).</b>
                    </div>
                </div>
            </div>
        </div>

        <div class="sop-container-card">
            <div style="font-size: 17px; font-weight: 800; color: #0F172A; margin-bottom: 12px;">
                1. Educational & Non-Diagnostic Purpose
            </div>
            <p style="font-size: 13px; color: #475569; line-height: 1.7; margin-bottom: 16px;">
                This software application, <b>CardioML</b>, was developed as an undergraduate coursework project for <b>Semester 5 Machine Learning (ML)</b> in accordance with the official <i>Standard Operating Procedure (SOP) for Student Project Allocation, Execution & Monitoring</i> issued by the Computer Engineering Department, Darshan University.
            </p>
            <p style="font-size: 13px; color: #475569; line-height: 1.7; margin-bottom: 16px;">
                The underlying models (Gradient Boosting & AdaBoost classifiers) are statistical inference engines trained on historical observational records from Kaggle's Cardiovascular Disease Dataset. <b>Under no circumstances does this application constitute medical diagnosis, clinical prescription, or doctor-patient privilege.</b>
            </p>

            <div style="font-size: 17px; font-weight: 800; color: #0F172A; margin: 24px 0 12px 0;">
                2. Data Privacy & Ethical Compliance
            </div>
            <p style="font-size: 13px; color: #475569; line-height: 1.7; margin-bottom: 16px;">
                In strict adherence to medical ethics and HIPAA/GDPR data protection principles:
            </p>
            <ul style="font-size: 13px; color: #475569; line-height: 1.8; margin-left: -10px; margin-bottom: 20px;">
                <li>No personally identifiable information (PII) like names, phone numbers, or addresses is collected or stored.</li>
                <li>Health vitals entered into the prediction form are processed ephemerally in-memory and discarded upon session completion.</li>
                <li>No user inputs are retained or written to external third-party tracking databases.</li>
            </ul>

            <div style="font-size: 17px; font-weight: 800; color: #0F172A; margin: 24px 0 12px 0;">
                3. Project Review & Department Sign-Off
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 14px;">
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px;">
                    <div style="font-size: 11px; font-weight: 700; color: #64748B; text-transform: uppercase;">Approved by HOD</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">Prof. Rupesh G Vaishnav</div>
                    <div style="font-size: 12px; color: #64748B;">Head of Department, Computer Engineering</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px;">
                    <div style="font-size: 11px; font-weight: 700; color: #64748B; text-transform: uppercase;">Approved by Dean</div>
                    <div style="font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 4px;">Dr. Gopi B Sanghani</div>
                    <div style="font-size: 12px; color: #64748B;">Dean, Faculty of Technology</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
