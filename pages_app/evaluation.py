"""
CardioPredict Model Evaluation Page.
Comprehensive performance benchmarking, overfitting audit,
5-fold cross validation consistency, hyperparameter tuning comparison,
and scratch algorithm verification.
Department of Computer Engineering, Darshan University.
Student: Veerbhadrasinh • Semester 5 Machine Learning
"""
import streamlit as st
import plotly.graph_objects as go
from components.charts import render_overfitting_chart, render_cv_chart
from components.banners import render_medical_disclaimer

def render():
    st.markdown("""<div style="margin-bottom: 32px;">
<div class="pro-badge">
<span class="pro-pulse-dot" style="background: #E11D48; box-shadow: 0 0 10px #E11D48;"></span> EMPIRICAL BENCHMARKS &bull; SOP AUDIT
</div>
<h1 style="font-size: 38px; font-weight: 800; color: #FFFFFF; letter-spacing: -1px; margin: 0 0 10px 0;">
Model Evaluation &amp; <span class="hero-heading-highlight">Validation Audit</span>
</h1>
<p style="font-size: 15px; color: #94A3B8; max-width: 780px; line-height: 1.6; margin: 0;">
Rigorous empirical benchmarking evaluating dual production ensembles (Random Forest &amp; AdaBoost), systematic hyperparameter tuning, overfitting audits, and pure NumPy scratch verification.
</p>
</div>""", unsafe_allow_html=True)

    tab_overview, tab_tuning, tab_definitions = st.tabs([
        "🏆 Dual Model Scorecard & Overfitting Audit",
        "⚙️ Hyperparameter Tuning (Random Forest vs AdaBoost)",
        "📖 Viva Voce Metric Definitions"
    ])

    with tab_overview:
        # -------------------------------------------------------------
        # 1. ADABOOST (DUAL ENSEMBLE PRODUCTION MODEL 1)
        # -------------------------------------------------------------
        st.markdown("""<div class="vercel-card" style="margin-bottom: 24px; border-left: 3px solid #10B981; padding: 26px 28px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 20px;">⚡</span>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">AdaBoost Classifier</span>
<span style="font-size: 10.5px; font-weight: 700; color: #34D399; background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.35); padding: 2px 9px; border-radius: 999px;">RECOMMENDED ENSEMBLE</span>
</div>
<div style="font-size: 12px; color: #94A3B8; font-family: monospace;">
n_estimators=100 &bull; learning_rate=1.0 &bull; random_state=42
</div>
</div>
<p style="font-size: 13.5px; color: #94A3B8; line-height: 1.7; margin-bottom: 20px;">
AdaBoost iteratively fits sequential decision stumps (depth=1), adaptively increasing the weights of previously misclassified patients. This produces well-calibrated decision margins with optimal generalization and minimal overfitting gap (0.64%) on standardized medical tabular features.
</p>""", unsafe_allow_html=True)

        m1, m2, m3, m4, m5 = st.columns(5)
        with m1:
            st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 28px;">72.5%</div>
<div class="stat-counter-label">Test Accuracy</div>
<div style="font-size: 11px; color: #10B981; margin-top: 4px;">Holdout Set</div>
</div>""", unsafe_allow_html=True)
        with m2:
            st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 28px;">76.2%</div>
<div class="stat-counter-label">Precision</div>
<div style="font-size: 11px; color: #38BDF8; margin-top: 4px;">Positive Predictivity</div>
</div>""", unsafe_allow_html=True)
        with m3:
            st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 28px;">65.3%</div>
<div class="stat-counter-label">Recall</div>
<div style="font-size: 11px; color: #F59E0B; margin-top: 4px;">Sensitivity</div>
</div>""", unsafe_allow_html=True)
        with m4:
            st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 28px;">70.3%</div>
<div class="stat-counter-label">F1-Score</div>
<div style="font-size: 11px; color: #A855F7; margin-top: 4px;">Harmonic Balance</div>
</div>""", unsafe_allow_html=True)
        with m5:
            st.markdown("""<div class="stat-counter-card">
<div class="stat-counter-num" style="font-size: 28px;">79.2%</div>
<div class="stat-counter-label">ROC-AUC</div>
<div style="font-size: 11px; color: #F43F5E; margin-top: 4px;">Class Separability</div>
</div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------------------------------------------------
        # 2. RANDOM FOREST & OVERFITTING DEMONSTRATION
        # -------------------------------------------------------------
        st.markdown("""<div class="vercel-card" style="margin-bottom: 24px; border-left: 3px solid #F43F5E; padding: 26px 28px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 20px;">🌲</span>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">Random Forest Classifier &amp; Overfitting Audit</span>
<span style="font-size: 10.5px; font-weight: 700; color: #FB7185; background: rgba(225,29,72,0.15); border: 1px solid rgba(225,29,72,0.35); padding: 2px 9px; border-radius: 999px;">SOP PHASE 8 AUDIT</span>
</div>
<div style="font-size: 12px; color: #94A3B8; font-family: monospace;">
Baseline vs Tuned Comparison
</div>
</div>
<p style="font-size: 13.5px; color: #94A3B8; line-height: 1.7; margin-bottom: 20px;">
Random Forest builds an ensemble of bootstrap-aggregated decision trees. When trees are grown without depth constraints, they memorize sample noise, achieving near 100% training score while test performance stagnates. Below is the empirical demonstration required by SOP Section 4.
</p>""", unsafe_allow_html=True)

        col_rf_c, col_rf_t = st.columns([1.5, 1.0])
        with col_rf_c:
            render_overfitting_chart(99.98, 71.56)

        with col_rf_t:
            st.markdown("""<div style="background: rgba(225, 29, 72, 0.08); border: 1px solid rgba(225, 29, 72, 0.3); border-radius: 14px; padding: 20px; height: 100%;">
<div style="font-size: 12px; font-weight: 800; color: #FDA4AF; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px;">
⚠️ Baseline Overfitting Audit Report
</div>
<div style="margin-bottom: 14px;">
<div style="display: flex; justify-content: space-between; font-size: 13.5px; color: #CBD5E1; margin-bottom: 8px;">
<span>Training Score (Memorization):</span>
<b style="font-family: monospace; color: #FB7185; font-size: 15px;">99.98%</b>
</div>
<div style="display: flex; justify-content: space-between; font-size: 13.5px; color: #CBD5E1; margin-bottom: 8px;">
<span>Test Holdout Score:</span>
<b style="font-family: monospace; color: #FFFFFF; font-size: 15px;">71.56%</b>
</div>
<div style="display: flex; justify-content: space-between; font-size: 14px; color: #FDA4AF; border-top: 1px solid rgba(225,29,72,0.3); padding-top: 8px;">
<span>Overfitting Score Gap:</span>
<b style="font-family: monospace; font-size: 16px; color: #F43F5E;">28.42%</b>
</div>
</div>
<div style="font-size: 12px; color: #94A3B8; line-height: 1.6;">
<b style="color: #FFFFFF;">Examiner Explanation:</b> Unconstrained tree growth allows deep nodes to isolate single training outliers. Tuning <code style="color: #FDA4AF; background: rgba(225,29,72,0.2); padding: 1px 5px; border-radius: 4px;">max_depth=15</code> and <code style="color: #FDA4AF; background: rgba(225,29,72,0.2); padding: 1px 5px; border-radius: 4px;">min_samples_leaf=5</code> eliminated this gap down to <b>4.55%</b> with <b>73.1%</b> test accuracy.
</div>
</div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------------------------------------------------
        # 3. 5-FOLD CROSS VALIDATION AUDIT
        # -------------------------------------------------------------
        st.markdown("""<div class="vercel-card" style="border-left: 3px solid #38BDF8; padding: 26px 28px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 20px;">🔄</span>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">5-Fold Stratified Cross-Validation Stability</span>
</div>
<div style="font-size: 12px; color: #38BDF8; font-family: monospace; font-weight: 600;">
5 Stratified Folds &bull; 70,000 Cohort
</div>
</div>
<p style="font-size: 13.5px; color: #94A3B8; line-height: 1.7; margin-bottom: 20px;">
The dataset was partitioned into 5 independent stratified folds to evaluate model resilience against sampling variance across different demographic subpopulations.
</p>""", unsafe_allow_html=True)

        col_cv_c, col_cv_t = st.columns([1.5, 1.0])
        with col_cv_c:
            render_cv_chart([71.44, 72.08, 71.30, 71.40, 72.17])

        with col_cv_t:
            st.markdown("""<div style="background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 14px; padding: 20px; height: 100%;">
<div style="font-size: 12px; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 14px;">
Cross-Validation Summary
</div>
<div style="margin-bottom: 14px;">
<div style="font-size: 12px; color: #94A3B8;">Average 5-Fold Score</div>
<div style="font-size: 28px; font-weight: 800; color: #FFFFFF; font-family: monospace; margin-top: 2px;">71.68%</div>
</div>
<div style="margin-bottom: 14px;">
<div style="font-size: 12px; color: #94A3B8;">Score Spread (Max - Min)</div>
<div style="font-size: 24px; font-weight: 800; color: #38BDF8; font-family: monospace; margin-top: 2px;">0.87%</div>
</div>
<div style="font-size: 12px; color: #CBD5E1; line-height: 1.6;">
The narrow spread of <b style="color: #FFFFFF;">0.87 percentage points</b> demonstrates high model stability across folds without catastrophic generalization collapse.
</div>
</div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with tab_tuning:
        # -------------------------------------------------------------
        # HYPERPARAMETER TUNING SECTION (SOP Phase 9)
        # -------------------------------------------------------------
        st.markdown("""<div class="vercel-card" style="padding: 28px 30px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
<span style="font-size: 22px;">⚙️</span>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">Systematic Hyperparameter Tuning (SOP Phase 9)</span>
</div>
<p style="font-size: 14px; color: #94A3B8; line-height: 1.7; margin-bottom: 22px;">
GridSearchCV was executed with 3-fold cross-validation strictly on the training partition. The untouched holdout test partition was preserved solely for final unbiased verification.
</p>
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left; margin-bottom: 14px;">
<thead>
<tr style="background: rgba(15, 23, 42, 0.9); border-bottom: 1px solid rgba(255, 255, 255, 0.12);">
<th style="padding: 12px 14px; color: #FFFFFF; font-weight: 700;">Model Configuration</th>
<th style="padding: 12px 14px; color: #FFFFFF; font-weight: 700;">Hyperparameters</th>
<th style="padding: 12px 14px; color: #FFFFFF; font-weight: 700;">Training Score</th>
<th style="padding: 12px 14px; color: #FFFFFF; font-weight: 700;">Test Accuracy</th>
<th style="padding: 12px 14px; color: #FFFFFF; font-weight: 700;">Overfitting Gap</th>
<th style="padding: 12px 14px; color: #FFFFFF; font-weight: 700;">Generalization Status</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 12px 14px; font-weight: 700; color: #FFFFFF;">Random Forest (Baseline)</td>
<td style="padding: 12px 14px; font-family: monospace; color: #94A3B8;">depth=None, leaf=1, n=100</td>
<td style="padding: 12px 14px; color: #FB7185; font-weight: 700;">99.98%</td>
<td style="padding: 12px 14px; font-weight: 700; color: #CBD5E1;">71.56%</td>
<td style="padding: 12px 14px; color: #F43F5E; font-weight: 800;">28.42% (High)</td>
<td style="padding: 12px 14px;"><span style="background: rgba(225,29,72,0.15); color: #FDA4AF; border: 1px solid rgba(225,29,72,0.3); padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;">Severe Overfitting</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(16, 185, 129, 0.05);">
<td style="padding: 12px 14px; font-weight: 700; color: #34D399;">Random Forest (Tuned)</td>
<td style="padding: 12px 14px; font-family: monospace; color: #CBD5E1;">depth=15, leaf=5, n=100</td>
<td style="padding: 12px 14px; color: #34D399; font-weight: 700;">77.76%</td>
<td style="padding: 12px 14px; color: #34D399; font-weight: 800;">73.21%</td>
<td style="padding: 12px 14px; color: #34D399; font-weight: 800;">4.55% (Fixed)</td>
<td style="padding: 12px 14px;"><span style="background: rgba(16,185,129,0.18); color: #34D399; border: 1px solid rgba(16,185,129,0.4); padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;">Optimal Generalization</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<td style="padding: 12px 14px; font-weight: 700; color: #FFFFFF;">AdaBoost (Baseline)</td>
<td style="padding: 12px 14px; font-family: monospace; color: #94A3B8;">n=100, lr=1.0</td>
<td style="padding: 12px 14px; font-weight: 700; color: #CBD5E1;">73.10%</td>
<td style="padding: 12px 14px; font-weight: 700; color: #CBD5E1;">72.46%</td>
<td style="padding: 12px 14px; color: #34D399; font-weight: 800;">0.64% (Minimal)</td>
<td style="padding: 12px 14px;"><span style="background: rgba(56,189,248,0.15); color: #38BDF8; border: 1px solid rgba(56,189,248,0.3); padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;">High Calibration</span></td>
</tr>
<tr>
<td style="padding: 12px 14px; font-weight: 700; color: #FFFFFF;">AdaBoost (Tuned)</td>
<td style="padding: 12px 14px; font-family: monospace; color: #94A3B8;">n=150, lr=1.0</td>
<td style="padding: 12px 14px; font-weight: 700; color: #CBD5E1;">73.18%</td>
<td style="padding: 12px 14px; font-weight: 700; color: #CBD5E1;">72.49%</td>
<td style="padding: 12px 14px; color: #34D399; font-weight: 800;">0.69% (Minimal)</td>
<td style="padding: 12px 14px;"><span style="background: rgba(56,189,248,0.15); color: #38BDF8; border: 1px solid rgba(56,189,248,0.3); padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700;">Stable Production</span></td>
</tr>
</table>
</div>
</div>""", unsafe_allow_html=True)

    with tab_definitions:
        # -------------------------------------------------------------
        # VIVA REFERENCE METRICS DEFINITIONS
        # -------------------------------------------------------------
        st.markdown("""<div class="vercel-card" style="padding: 28px 30px;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
<span style="font-size: 22px;">📖</span>
<span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">Viva Voce Metric Definitions &amp; Clinical Formulas</span>
</div>
<p style="font-size: 14px; color: #94A3B8; line-height: 1.6; margin-bottom: 22px;">
Examiner reference guide explaining binary classification evaluation metrics and clinical trade-offs.
</p>""", unsafe_allow_html=True)

        d1, d2, d3, d4 = st.columns(4)
        with d1:
            st.markdown("""<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 18px; height: 100%;">
<div style="font-size: 14.5px; font-weight: 800; color: #10B981; margin-bottom: 4px;">Accuracy</div>
<div style="font-size: 11px; color: #94A3B8; font-family: monospace; margin-bottom: 8px;">(TP + TN) / Total</div>
<div style="font-size: 12.5px; color: #CBD5E1; line-height: 1.6;">
Fraction of total cases correctly identified. Evaluates overall baseline correctness across balanced distributions.
</div>
</div>""", unsafe_allow_html=True)

        with d2:
            st.markdown("""<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 18px; height: 100%;">
<div style="font-size: 14.5px; font-weight: 800; color: #38BDF8; margin-bottom: 4px;">Precision</div>
<div style="font-size: 11px; color: #94A3B8; font-family: monospace; margin-bottom: 8px;">TP / (TP + FP)</div>
<div style="font-size: 12.5px; color: #CBD5E1; line-height: 1.6;">
Positive predictivity: Out of all patients flagged as high risk, what fraction truly have cardiovascular pathology.
</div>
</div>""", unsafe_allow_html=True)

        with d3:
            st.markdown("""<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 18px; height: 100%;">
<div style="font-size: 14.5px; font-weight: 800; color: #F59E0B; margin-bottom: 4px;">Recall (Sensitivity)</div>
<div style="font-size: 11px; color: #94A3B8; font-family: monospace; margin-bottom: 8px;">TP / (TP + FN)</div>
<div style="font-size: 12.5px; color: #CBD5E1; line-height: 1.6;">
Clinical safety measure: Out of all truly diseased individuals, how many were caught without dangerous false negatives.
</div>
</div>""", unsafe_allow_html=True)

        with d4:
            st.markdown("""<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 18px; height: 100%;">
<div style="font-size: 14.5px; font-weight: 800; color: #A855F7; margin-bottom: 4px;">F1-Score</div>
<div style="font-size: 11px; color: #94A3B8; font-family: monospace; margin-bottom: 8px;">2 &times; (P &times; R) / (P + R)</div>
<div style="font-size: 12.5px; color: #CBD5E1; line-height: 1.6;">
Harmonic mean balancing precision and recall, guarding against false reassurance in population pre-screening.
</div>
</div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    render_medical_disclaimer()
