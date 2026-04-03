import streamlit as st
from form import show_form
from interview import show_interview
from chatbot import show_chatbot
from greeting import show_greeting
from result import show_result
import time

if "page" not in st.session_state:
    st.session_state.page = "greeting"

# 🔥 GLOBAL PLACEHOLDER (KEY FIX)
placeholder = st.empty()

# ---------------- ROUTING ---------------- #

if st.session_state.page == "greeting":
    with placeholder.container():
        show_greeting()

elif st.session_state.page == "form":
    with placeholder.container():
        show_form()

elif st.session_state.page == "loading":
    # 🔥 CLEAR EVERYTHING
    placeholder.empty()

    # Blank screen
    time.sleep(1) 

    st.session_state.page = "interview"
    st.rerun()

elif st.session_state.page == "interview":
    with placeholder.container():
        show_interview()

elif st.session_state.page == "chatbot":
    with placeholder.container():
        show_chatbot()

elif st.session_state.page == "loading_chatbot":
    placeholder.empty()
    st.markdown("<h3 style='text-align:center;'>🤖 Preparing your interview...</h3>", unsafe_allow_html=True)
    time.sleep(1.5)
    st.session_state.page = "chatbot"
    st.rerun()

elif st.session_state.page == "result":
    with placeholder.container():
        show_result()