import streamlit as st
import re
import tempfile
import os
from report import generate_pdf


def extract_score(report):
    patterns = [
        r'FINAL SCORE:\s*(\d+)\s*/\s*10',
        r'FINAL SCORE:\s*(\d+)',
        r'(\d+)\s*/\s*10'
    ]

    for pattern in patterns:
        match = re.search(pattern, report, re.IGNORECASE)
        if match:
            return int(match.group(1))

    return 0


def extract_result(report):
    score = extract_score(report)

    if score >= 8:
        return "Very Excellent"
    elif score >= 5:
        return "Good"
    else:
        return "Needs Improvement"

    # fallback using score
    score = extract_score(report)
    return "Very Excellent" if score >= 7 else "Needs Improvement"


def extract_summary(report):
    match = re.search(r'FINAL SUMMARY:\s*(.*?)(FINAL SCORE:|RESULT:)', report, re.DOTALL)
    return match.group(1).strip() if match else report

def extract_section(report, section_name):
    pattern = rf"{section_name}:\s*(.*?)(?:\n[A-Z][A-Z ]+:|\Z)"
    match = re.search(pattern, report, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""

def show_result():

    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #020617, #0f172a);
    }

    /* Card */
    .card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 25px;
        border: 1px solid rgba(148, 163, 184, 0.1);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.1);
        margin-bottom: 20px;
    }

    /* Score Box */
    .score-box {
        width: 150px;
        height: 150px;
        border-radius: 20px;
        border: 3px solid #38bdf8;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        font-weight: bold;
        color: white;
        margin: auto;
    }

    /* Tag */
    .tag {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: #22c55e;
        color: white;
        font-size: 12px;
        margin-top: 10px;
    }

    /* Section title */
    .section-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Progress bar */
    .bar {
        height: 6px;
        background: #1e293b;
        border-radius: 10px;
        overflow: hidden;
    }

    .fill {
        height: 100%;
    }

    .fill.green { background: #22c55e; }
    .fill.blue { background: #38bdf8; }
    .fill.orange { background: #f59e0b; }
    .fill.purple { background: #a855f7; }

    .label {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 8px;
    }

    .summary {
        color: #e2e8f0;
        line-height: 1.6;
        font-size: 14px;
    }

    .card {
        margin-bottom: 25px;
    }   

    </style>
    """, unsafe_allow_html=True)

    st.title("📊 Final Interview Result")

    report = st.session_state.get("final_report", "")

    if not report:
        st.error("⚠️ No report found. Please complete the interview first.")
        return

    # ---------------- EXTRACT DATA ---------------- #
    score = extract_score(report)
    result_text = extract_result(report)
    summary = extract_summary(report)

    strengths = extract_section(report, "STRENGTHS")
    improvements = extract_section(report, "AREAS TO IMPROVE")
    suggestions = extract_section(report, "SUGGESTIONS")
    skills = extract_section(report, "SKILL BREAKDOWN")
    if not skills:
        skills = extract_section(report, "SKILL BREAKDOWN (MANDATORY)")
    if not skills:
        skills = "Not Available"
    next_steps = extract_section(report, "NEXT STEPS")
    if not next_steps:
        next_steps = "You will be contacted by our team for further evaluation."

    # ---------------- SCORE COLOR ---------------- #
    if score >= 8:
        score_class = "good"
    elif score >= 5:
        score_class = "avg"
    else:
        score_class = "bad"

    # ---------------- SCORE CARD ---------------- #
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <div class="score-box">{score}<br><span style="font-size:12px; color:#94a3b8;">OUT OF 10</span></div>
        <div class="tag">{result_text.upper()}</div>
        <p style="margin-top:10px; color:#94a3b8;">
            {"Excellent performance with strong fundamentals." if score >= 8 else "Good effort, keep improving your fundamentals."}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- SUMMARY CARD ---------------- #
    st.markdown("""
    <div class="card">
        <div class="label">🧠 AI Feedback</div>
    """, unsafe_allow_html=True)

    st.markdown(f"<div class='summary'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- STRENGTHS/IMPROVEMENTS/SUGGESTIONS ---------------- #
    def render_box(title, content):
        return f"""
        <div class="card">
            <div class="section-title">{title}</div>
            <div class="summary">{content}</div>
        </div>
        """

    if strengths:
        st.markdown(render_box("💪 Key Strengths", strengths), unsafe_allow_html=True)

    if improvements:
        st.markdown(render_box("📉 Areas to Improve", improvements), unsafe_allow_html=True)

    if suggestions:
        st.markdown(render_box("📌 Suggestions", suggestions), unsafe_allow_html=True)

    # ---------------- SKILL BREAKDOWN ---------------- #
    def render_skill(skill, value):

        color = "green"
        if value < 75:
            color = "orange"
        elif value < 85:
            color = "blue"

        return f"""
        <div style="margin-bottom:12px;">
            <div style="display:flex; justify-content:space-between;">
                <span>{skill}</span>
                <span>{value}%</span>
            </div>
            <div class="bar">
                <div class="fill {color}" style="width:{value}%"></div>
            </div>
        </div>
        """

    if skills and skills != "Not Available":

        st.markdown('<div class="card"><div class="section-title">🧩 Skill Breakdown</div>', unsafe_allow_html=True)

        lines = skills.split("\n")

        for line in lines:
            match = re.search(r'(.+):\s*(\d+)', line.strip())
            if match:
                skill_name = match.group(1).strip()
                score_val = int(match.group(2))
                if score_val <= 10:
                    score_val *= 10
                st.markdown(render_skill(skill_name, score_val), unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="card">
            <div class="label">🧩 Skill Breakdown</div>
            <div class="summary">Not Available</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- NEXT STEPS ---------------- #
    if next_steps:
        st.markdown(f"""
        <div class="card" style="border:1px solid #22c55e; background:rgba(34,197,94,0.05);">
            <div class="section-title">📢 Next Steps</div>
            <div style="font-size:16px; font-weight:600; color:#22c55e;">
                {next_steps}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- FINAL CTA ---------------- #
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h3>Interview Completed Successfully</h3>
        <p style="color:#94a3b8;">Your performance report is ready for review.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ---------------- ACTION BUTTONS ---------------- #
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔄 Start New Interview", use_container_width=True):
            st.session_state.clear()
            st.session_state.page = "form"
            st.rerun()

    with col2:
        st.download_button(
            label="📄 Download TXT",
            data=report,
            file_name="interview_report.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col3:
        if st.button("📥 Download PDF", use_container_width=True):
            data = {
                "name": f"{st.session_state.get('first_name', '')} {st.session_state.get('last_name', '')}",
                "role": st.session_state.get("role", "Unknown"),
                "score": score,
                "result": result_text,
                "summary": summary,
                "strengths": strengths,
                "improvements": improvements,
                "suggestions": suggestions,
                "skills": skills,
                "next_steps": next_steps
            }

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp_path = tmp.name

            generate_pdf(tmp_path, data)

            with open(tmp_path, "rb") as f:
                pdf_bytes = f.read()

            os.unlink(tmp_path)

            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name="interview_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )
