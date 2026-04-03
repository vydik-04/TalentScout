# 🤖 TalentScout AI Hiring Assistant

    An AI-powered interview platform that simulates real-world technical interviews — with personalized questions, live evaluation, and a detailed performance report at the end.
---

## 🚀 Features

    - 🎯 Role and tech stack based AI interview
    - 💬 Chatbot-style conversational interview flow
    - 📊 Short evaluation after every answer
    - 🧠 Context-aware follow-up questions
    - 🛡️ Guard against premature final summary generation
    - 📄 Final performance report with score, strengths, skill breakdown, and suggestions
    - ⏳ Animated countdown timer before the interview starts
    - 🎨 Clean multi-page UI — Greeting → Form → Countdown → Interview → Result
    - 📥 Download your report as a `.txt` file
    - 🔄 Start a new interview anytime from the result page

---

## 🧩 Project Structure
    TalentScout-Chatbot/
    │
    ├── app.py              # Main routing and page navigation
    ├── greeting.py         # Welcome/landing page
    ├── form.py             # Multi-step candidate details form
    ├── interview.py        # Countdown timer and interview start screen
    ├── chatbot.py          # AI interview chat interface
    ├── ai_engine.py        # Ollama API integration (LLaMA 3)
    ├── result.py           # Final result display with skill breakdown
    ├── report.py           # PDF report generation (ReportLab)
    ├── data.py             # Job departments, domains, roles, tech suggestions
    ├── requirements.txt    # Python dependencies
    └── README.md           # Project documentation

---

## 🛠️ Tech Stack

    | Layer | Technology |
    |---|---|
    | UI / Frontend | Streamlit |
    | Backend | Python |
    | AI Model | Ollama (LLaMA 3) |
    | PDF Generation | ReportLab |
    | Styling | Custom CSS via `st.markdown` |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
    ```bash
    git clone https://github.com/your-username/TalentScout-Chatbot.git
    cd TalentScout-Chatbot
    ```

### 2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

### 3. Install and set up Ollama

    Download Ollama from https://ollama.com and install it, then pull the model:
        ```bash
        ollama pull llama3
        ```

    Start the model server:
        ```bash
        ollama run llama3
        ```

        Make sure Ollama is running on `http://127.0.0.1:11434` before launching the app. You can verify this by visiting that URL in your browser — it should return a response.

### 4. Run the application
    ```bash
    streamlit run app.py
    ```
---

## 🗺️ Application Flow
    Greeting Page
    ↓
    Candidate Form (multi-step)
    → First name, middle name, last name
    → Email
    → Country code + phone number
    → Years of experience
    → Current location
    → Department → Domain → Role
    → Tech stack selection
    ↓
    Countdown Screen (10 seconds with skip option)
    ↓
    AI Interview (chatbot)
    Stage 1 → "Tell me about yourself"
    Stage 2 → "Tell me about the best project you've worked on"
    Stage 3 → Tech stack questions (easy → medium → hard)
    Stage 4 → Real-world scenario questions
    Stage 5 → "Do you have any questions for me?"
    ↓
    Final Result Page
    → Score, result, summary
    → Strengths, areas to improve, suggestions
    → Skill breakdown with progress bars
    → Next steps
    → Download report as .txt

---

## 🤖 AI Interview Behaviour

    - Asks exactly one question at a time
    - Gives 2–3 lines of feedback after every answer
    - Asks a follow-up if the answer is too shallow
    - Never reveals the score during the interview
    - Only generates the final summary after the candidate explicitly confirms they have no more questions
    - Guards against the model generating the summary too early
    - Ignores off-topic questions and redirects to the interview

---

## 📄 Final Report Format

    The report generated at the end of the interview follows this exact structure:
    FINAL SUMMARY:
        <overall performance in 3–4 lines>
    FINAL SCORE:
        <score>/10
    RESULT:
        Very Excellent / Needs Improvement
    STRENGTHS:

        point 1
        point 2

    AREAS TO IMPROVE:

        point 1
        point 2

    SUGGESTIONS:

        point 1
        point 2

    SKILL BREAKDOWN:

        <tech>: <score>/10
        <tech>: <score>/10
        <tech>: <score>/10

    NEXT STEPS:
        You will be contacted by our team for further evaluation.
        Wish you luck for your upcoming opportunities.
        No matter what the result is, stay strong and keep trying.

---

## 🧾 Form Validations

    Every field in the candidate form is validated before moving to the next step:

    | Field | Rule |
    |---|---|
    | First name | 2–30 alphabets only, no spaces |
    | Middle name | Optional, 1–30 alphabets |
    | Last name | 1–30 alphabets only |
    | Email | Standard format — example@domain.com |
    | Country code | Must start with `+`, 1–3 digits (e.g. `+91`) |
    | Phone | Exactly 10 digits, no country code |
    | Experience | 0 to 40, decimals allowed (e.g. `2.5`) |
    | Location | 2–50 alphabets and spaces only |
    | Tech stack | At least one skill required |

---

## ⚠️ Known Limitations

    - Requires Ollama to be running locally — the app will not work without it
    - No authentication or user account system
    - No tab-switch detection or proctoring (Streamlit limitation)
    - AI response quality depends on the local model (LLaMA 3 via Ollama)
    - Session state resets on browser refresh — the interview cannot be resumed

---

## 🚀 Planned Improvements

    - 🎤 Voice input support
    - 🎥 Webcam monitoring during the interview
    - ☁️ Cloud deployment (Streamlit Cloud / AWS)
    - 📊 Admin dashboard to review multiple candidates
    - 📈 Performance analytics across sessions
    - 🌐 OpenAI / Gemini as optional AI backends

---

## ⭐ Acknowledgements

    - [Streamlit](https://streamlit.io) — UI framework
    - [Ollama](https://ollama.com) — local LLM server
    - [LLaMA 3](https://ai.meta.com/llama/) — underlying AI model
    - [ReportLab](https://www.reportlab.com) — PDF generation

---

## 📌 Note

This project was built as part of an AI/ML assignment to demonstrate:

    - End-to-end AI application development
    - Prompt engineering for structured interview behaviour
    - Multi-step form design with validation and edit support
    - Clean, responsive UI using Streamlit and custom CSS

---

## 🔒 Data Privacy & Security

    - This application does NOT store any user data permanently.
    - All candidate information is stored temporarily using Streamlit session state.
    - Data is automatically cleared once the session ends or the user restarts the interview.
    - No external database or third-party storage is used.
    - The application ensures minimal data exposure and follows basic privacy best practices.
    - Sensitive information (email, phone) is used only for simulation purposes and not transmitted externally.
