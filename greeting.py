import streamlit as st

def show_greeting():
    # ---------------- GLOBAL STYLE ---------------- #
    st.markdown("""
    <style>
    /* Center the entire content */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-family: 'Inter', sans-serif;
    }

    .title-text {
        font-size: 42px;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 10px;
        margin-bottom: 0px;
    }

    .subtitle-text {
        font-size: 18px;
        color: #94a3b8;
        margin-bottom: 40px;
    }

    /* Grid Card Styling */
    .card {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        text-align: left;
        height: 140px;
    }

    .card-icon { font-size: 24px; margin-bottom: 10px; }
    .card-title { font-size: 16px; font-weight: 700; color: #FFFFFF; }
    .card-desc { font-size: 13px; color: #64748b; margin-top: 5px; }

    /* Instruction Box Styling */
    .info-box {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 25px;
        text-align: left;
        width: 100%;
        margin-top: 20px;
    }

    .info-title {
        font-size: 14px;
        font-weight: 700;
        color: #3b82f6;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }

    .info-item {
        font-size: 15px;
        color: #cbd5e1;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
    }

    /* Button Styling to match blue primary */
    div.stButton > button:first-child {
        background-color: #3b82f6;
        color: white;
        border: none;
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-weight: 600;
        font-size: 16px;
        margin-top: 20px;
    }
    
    .footer-text {
        font-size: 12px;
        color: #475569;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- LAYOUT ---------------- #
    
    # 1. Header Section
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=60) # Placeholder for the Robot Icon
    st.markdown('<p class="title-text">TalentScout AI Interview</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Your intelligent interview assistant — powered by AI</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Features Grid (2x2)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('''<div class="card">
            <div class="card-icon">⚡</div>
            <div class="card-title">AI-Powered</div>
            <div class="card-desc">Smart questions tailored to your tech stack</div>
        </div>''', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('''<div class="card">
            <div class="card-icon">🎯</div>
            <div class="card-title">Personalized</div>
            <div class="card-desc">Adaptive difficulty based on responses</div>
        </div>''', unsafe_allow_html=True)

    with col2:
        st.markdown('''<div class="card">
            <div class="card-icon">📊</div>
            <div class="card-title">Real-time Eval</div>
            <div class="card-desc">Instant scoring and analysis</div>
        </div>''', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('''<div class="card">
            <div class="card-icon">🛡️</div>
            <div class="card-title">Detailed Report</div>
            <div class="card-desc">Comprehensive performance breakdown</div>
        </div>''', unsafe_allow_html=True)

    # 3. "What to Expect" Box
    st.markdown('''<div class="info-box">
        <div class="info-title">What to Expect</div>
        <div class="info-item">💬 &nbsp; Conversational interview through chat</div>
        <div class="info-item">⚙️ &nbsp; Questions on your declared tech stack</div>
        <div class="info-item">📊 &nbsp; Score and feedback after each answer</div>
        <div class="info-item">🕒 &nbsp; ~15 minutes for a full interview</div>
    </div>''', unsafe_allow_html=True)

    # 4. Instructions Box
    st.markdown('''<div class="info-box">
        <div class="info-title">Instructions</div>
        <div class="info-item">🔹 Answer clearly and confidently</div>
        <div class="info-item">🔹 Stay focused during the interview</div>
        <div class="info-item">🔹 Think before responding</div>
        <div class="info-item">🔹 Take your time — there's no rush</div>
    </div>''', unsafe_allow_html=True)

    # 5. Start Button
    if st.button("🚀 Start Interview"):
        st.session_state.page = "form"
        st.rerun()

    # 6. Footer
    st.markdown('<div class="main-container"><p class="footer-text">This interview evaluates your practical and conceptual understanding.</p></div>', unsafe_allow_html=True)