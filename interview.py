import streamlit as st
import time

def show_interview():
    # 1. Protection Gate
    if st.session_state.get("page") != "interview":
        return

    # ---------------- GLOBAL EDITORIAL STYLING ---------------- #
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Inter:wght@400;500;600&display=swap');

    .stApp {
        background-color: #0d1117;
    }
    
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-family: 'Inter', sans-serif;
        color: #FFFFFF;
        padding-top: 60px;
    }

    .title-text {
        font-family: 'Manrope', sans-serif;
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -2px;
        color: #ffffff;
    }

    .subtitle-text {
        font-size: 18px;
        color: #8b949e;
        margin-bottom: 50px;
    }

    /* Circular Countdown Ring */
    .timer-container {
        position: relative;
        width: 260px;
        height: 260px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
    }

    .timer-circle {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 4px solid #1f2937;
        border-top: 4px solid #38bdf8;
        border-right: 4px solid #818cf8;
    }

    .timer-number {
        font-family: 'Manrope', sans-serif;
        font-size: 90px;
        font-weight: 800;
        line-height: 1;
    }

    .timer-label {
        font-size: 14px;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: 5px;
    }

    /* Tips Grid */
    .tips-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        max-width: 550px;
        margin-bottom: 40px;
    }

    .tip-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 18px 20px;
        display: flex; align-items: center; gap: 12px;
        font-size: 15px; color: #c9d1d9; text-align: left;
    }
    
    /* TARGET SKIP BUTTON SPECIFICALLY */
    div[data-testid="stButton"] > button {
        border: none !important;
        background: transparent !important;
        color: #58a6ff !important;
        text-decoration: underline !important;
        transition: 0.3s;
    }

    /* PRIMARY START BUTTON STYLING */
    .start-btn-container div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
        color: white !important;
        text-decoration: none !important;
        padding: 14px 45px !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        width: auto !important;
    }

    .success-icon-container {
        background-color: rgba(6, 95, 70, 0.2);
        color: #34d399;
        width: 90px; height: 90px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 44px; margin-bottom: 25px;
        border: 2px solid #065f46;
    }

    .footer-note { font-size: 13px; color: #484f58; margin-top: 30px; }
    </style>
    """, unsafe_allow_html=True)

    # 2. Timer Setup
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = time.time()

    duration = 10 
    elapsed = int(time.time() - st.session_state.timer_start)
    remaining = duration - elapsed

    placeholder = st.empty()

    if remaining > 0:
        with placeholder.container():
            st.markdown(f"""
            <div class="main-container">
                <div class="title-text">AI Interview Round</div>
                <div class="subtitle-text">Get ready — your interview begins soon</div>
                <div class="timer-container">
                    <div class="timer-circle"></div>
                    <div>
                        <div class="timer-number">{remaining}</div>
                        <div class="timer-label">Seconds</div>
                    </div>
                </div>
                <div class="tips-grid">
                    <div class="tip-card">🎯 Stay focused and confident</div>
                    <div class="tip-card">💡 Think before you answer</div>
                    <div class="tip-card">🗣️ Speak clearly and concisely</div>
                    <div class="tip-card">🧠 Structure your responses</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # REMOVED kind="secondary" to fix the error
            if st.button("Skip countdown"):
                st.session_state.timer_start = time.time() - duration
                st.rerun()

            st.markdown('<div class="main-container"><div class="footer-note">💪 All the best — you\'ve got this!</div></div>', unsafe_allow_html=True)
        
        time.sleep(1)
        st.rerun()

    else:
        # 3. Success State
        placeholder.empty()
        st.markdown("""
        <div class="main-container" style="padding-top: 100px;">
            <center><div class="success-icon-container">✓</div></center>
            <div class="title-text">Interview Started!</div>
            <div class="subtitle-text" style="max-width: 450px; margin: auto;">
                You're live. Take a deep breath, stay calm, and give it your best shot. 🚀
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="start-btn-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            if st.button("Enter Chatbot →", use_container_width=True):
                st.session_state.pop("timer_start", None)
                st.session_state.page = "loading_chatbot"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="main-container"><div class="footer-note">💪 All the best — you\'ve got this!</div></div>', unsafe_allow_html=True)
        