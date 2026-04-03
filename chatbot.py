import streamlit as st
from ai_engine import chat_with_ai
import re

# ---------------- CONFIG ---------------- #
MAX_HISTORY = 20

def show_chatbot():

    st.title("🤖 TalentScout AI Interview")

    if st.session_state.get("interview_completed"):
        st.success("✅ Interview completed!")
        if st.button("📊 View Result"):
            st.session_state.page = "result"
            st.rerun()
        return

    # ---------------- SAFE SESSION VALUES ---------------- #
    first_name = st.session_state.get("first_name", "Candidate")
    role = st.session_state.get("role", "Unknown Role")
    tech_stack = st.session_state.get("tech_stack", [])

    if "allow_final" not in st.session_state:
        st.session_state.allow_final = False

    # ---------------- INIT ---------------- #
    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

        system_prompt = f"""
You are a professional AI interviewer conducting a structured technical interview.

════════════════════════════════════════
IDENTITY & BOUNDARIES
════════════════════════════════════════
- You are ONLY an interviewer. You do NOT help, teach, or answer questions.
- If the candidate asks anything unrelated to the interview, respond EXACTLY:
  "I cannot answer that right now. Let's stay focused on the interview. We can discuss other topics afterward."
  Then immediately ask the next interview question.
- Stay in character at all times. No exceptions.

════════════════════════════════════════
CANDIDATE DETAILS
════════════════════════════════════════
Name       : {first_name}
Role       : {role}
Tech Stack : {', '.join(tech_stack)}

════════════════════════════════════════
FIRST MESSAGE RULE
════════════════════════════════════════
- Briefly introduce yourself as an AI interviewer (1–2 lines).
- Then ask ONLY: "Tell me about yourself."

════════════════════════════════════════
QUESTION RULES (APPLY THROUGHOUT)
════════════════════════════════════════
- Ask ONLY ONE question at a time. Never ask two questions together.
- After each answer:
    1. Give short feedback (2–3 lines max).
    2. Ask the next question.
- If an answer is too shallow, ask ONE follow-up before moving on.
- NEVER reveal scores during the interview.

════════════════════════════════════════
RESPONSE FORMAT RULES (APPLY THROUGHOUT)
════════════════════════════════════════
Every response during the interview MUST contain ONLY:
  • A short evaluation of the previous answer (2–3 lines)
  • The next question

DO NOT include:
  • Labels like "Evaluation:" or "Next Question:"
  • Explanations of your process
  • Any extra formatting or commentary

════════════════════════════════════════
INTERVIEW STAGES (FOLLOW IN STRICT ORDER)
════════════════════════════════════════

── STAGE 1: INTRODUCTION ──────────────
- Ask ONLY: "Tell me about yourself."
- Do NOT evaluate this answer. Move directly to Stage 2.

── STAGE 2: PROJECT DISCUSSION ────────
- Ask about the candidate's main project.
- Ask 1–2 questions total covering:
    • The problem it solved
    • Their approach
    • Challenges they faced
- Then move to Stage 3.

── STAGE 3: TECH STACK QUESTIONS ──────
- Ask exactly 3–4 questions based on: {', '.join(tech_stack)}
- Increase difficulty progressively:
    Q1 → Easy (basic concept/definition)
    Q2 → Medium (how/why it works)
    Q3 → Hard (trade-offs, internals, edge cases)
    Q4 → Hard (optional follow-up if needed)
- Focus on concepts, reasoning, and practical understanding.
- Then move to Stage 4.

── STAGE 4: SCENARIO-BASED QUESTIONS ──
- Ask 2–3 practical, real-world scenario questions.
- Focus on:
    • Problem-solving approach
    • Decision-making under constraints
    • Real-world thinking and trade-offs
- Then move to Stage 5.

── STAGE 5: CLOSING ───────────────────
- Ask EXACTLY: "Do you have any questions for me?"
- WAIT for the candidate's response. Do NOT generate the Final Summary yet.
- If they have questions:
    • Answer briefly (2–3 lines).
    • Then ask: "Do you have any other questions?"
    • Repeat until they confirm no more questions.
- Only proceed to Final Summary when the candidate says something like:
  "no", "nope", "nothing", "that's all", "I'm good", or equivalent.

════════════════════════════════════════
FINAL SUMMARY (ONLY AFTER STAGE 5 CONFIRMED)
════════════════════════════════════════
Output EXACTLY the following block. Do NOT skip any section. Do NOT add extra text.

FINAL SUMMARY:
<Overall performance assessment in 3–4 lines>

FINAL SCORE:
<score>/10

RESULT:
<Very Excellent / Needs Improvement>

STRENGTHS:
- <point 1>
- <point 2>

AREAS TO IMPROVE:
- <point 1>
- <point 2>

SUGGESTIONS:
- <point 1>
- <point 2>

SKILL BREAKDOWN:
- <tech from stack>: <score>/10
- <tech from stack>: <score>/10
- <tech from stack>: <score>/10
(Minimum 3 skills from {', '.join(tech_stack)} — this section is COMPULSORY)

NEXT STEPS:
You will be contacted by our team for further evaluation.
Wish you luck for your upcoming opportunities.
No matter what the result is, stay strong and keep trying.

════════════════════════════════════════
FINAL SUMMARY STRICT RULES
════════════════════════════════════════
- DO NOT say thank you, goodbye, or add any closing remarks.
- DO NOT output the Final Summary before Stage 5 is complete.
- DO NOT assume the interview is over until the candidate explicitly confirms no more questions.
- ALL 8 sections are MANDATORY: FINAL SUMMARY, FINAL SCORE, RESULT, STRENGTHS, AREAS TO IMPROVE, SUGGESTIONS, SKILL BREAKDOWN, NEXT STEPS.
- SKILL BREAKDOWN must contain at least 3 skills. Do NOT skip it.
"""

        st.session_state.system_prompt = system_prompt
        st.session_state.chat_history = []

        try:
            first_q = chat_with_ai([
                {"role": "system", "content": st.session_state.system_prompt},
                {"role": "system", "content": "Start the interview now. Follow FIRST MESSAGE RULE."}
            ])
        except Exception:
            first_q = "⚠️ Unable to start interview. Please refresh."

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": first_q
        })

        st.rerun()

    # ---------------- DISPLAY CHAT ---------------- #
    for msg in st.session_state.chat_history:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # ---------------- INPUT ---------------- #
    if not st.session_state.get("interview_completed"):
        user_input = st.chat_input("Type your answer...")
    else:
        user_input = None

    if user_input and user_input.strip():

        if len(user_input.strip()) < 3:
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": "That seems a bit short. Could you please elaborate your answer?"
            })
            st.rerun()
            return

        clean_input = user_input.lower().strip()

        # ---------------- EXIT CONDITION ---------------- #
        if clean_input in ["exit", "quit", "bye"]:
            st.session_state.interview_completed = True     
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": "Interview terminated."
            })
            st.rerun()
            return

        # ---------------- FORCE FINAL IF USER SAYS NO ---------------- #
        no_keywords = ["no", "nope", "nothing", "none", "all good", "i'm fine", "im fine",
                       "not really", "that's all", "im good", "i'm good", "no thanks", "no questions"]

        is_no = any(kw in clean_input for kw in no_keywords) and len(clean_input.split()) <= 8

        if is_no:

            st.session_state.allow_final = True

            techs = st.session_state.get("tech_stack", ["Skill1", "Skill2", "Skill3"])
            fallback_skills = "\n".join([f"- {tech}: 7/10" for tech in techs[:3]])

            force_call = [{"role": "system", "content": st.session_state.system_prompt}] \
                       + st.session_state.chat_history[-MAX_HISTORY:] \
                       + [{
                            "role": "system",
                            "content": f"""
User confirmed no more questions. Output FINAL SUMMARY block now.
ALL 8 sections are mandatory. Do NOT skip any.

SKILL BREAKDOWN must use the candidate's actual tech stack:
{fallback_skills}
                            """
                        }]

            with st.spinner("Generating final result..."):
                bot_reply = chat_with_ai(force_call)

            st.session_state.final_report = bot_reply
            st.session_state.interview_completed = True
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": bot_reply
            })
            st.rerun()
            st.stop()

        # ---------------- AI RESPONSE ---------------- #
        try:
            with st.spinner("Thinking..."):

                call_history = [
                    {"role": "system", "content": st.session_state.system_prompt}
                ] + st.session_state.chat_history[-MAX_HISTORY:]

                user_lower = user_input.lower()
                meta_questions = ["how many", "how long", "questions left", "when will"]

                if any(q in user_lower for q in meta_questions):
                    call_history.append({
                        "role": "system",
                        "content": "User is asking about interview progress. Respond ONLY with: 'We are progressing well. Let's continue.' Then immediately ask the NEXT interview question."
                    })

                bot_reply = chat_with_ai(call_history).strip()

            # ---------------- FINAL SUMMARY GUARD ---------------- #
            if "final summary" in bot_reply.lower():

                if not st.session_state.get("allow_final"):
                    bot_reply = "Good answer! Let's keep going."
                    st.session_state.chat_history.append({
                        "role": "system",
                        "content": "Do NOT generate the FINAL SUMMARY yet. The candidate has not confirmed they have no more questions. Continue the interview from where you left off."
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": bot_reply
                    })
                    st.rerun()
                    st.stop()

                # allow_final is True — legitimate summary
                techs = st.session_state.get("tech_stack", ["Skill1", "Skill2", "Skill3"])
                fallback_skills = "\n".join([f"- {tech}: 7/10" for tech in techs[:3]])

                if "skill breakdown" not in bot_reply.lower():
                    bot_reply += f"\n\nSKILL BREAKDOWN:\n{fallback_skills}"

                bot_reply = re.sub(r"Do you have any questions.*", "", bot_reply, flags=re.IGNORECASE)
                bot_reply = re.sub(r"Well.*interview.*", "", bot_reply, flags=re.IGNORECASE)
                bot_reply = re.sub(r"Let's move on.*", "", bot_reply, flags=re.IGNORECASE)

                st.session_state.final_report = bot_reply
                st.session_state.interview_completed = True
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": bot_reply
                })
                st.rerun()
                st.stop()

            # ---------------- NORMAL RESPONSE ---------------- #
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": bot_reply
            })
            st.rerun()

        except Exception as e:
            st.error(f"⚠️ Error contacting AI: {str(e)}")
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": "⚠️ I'm having trouble connecting. Could you please repeat that?"
            })
            st.rerun()