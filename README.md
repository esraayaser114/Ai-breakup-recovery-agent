# Ai-breakup-recovery-agent
# 💔 Breakup Recovery Squad

An AI-powered emotional recovery web app that helps users process breakups through empathy, clarity, structure, and honest reflection. The system orchestrates multiple specialized AI agents to deliver emotional support, closure writing, recovery planning, and grounded reality checks — all in one private, user-controlled experience.

---

## 🧠 Project Overview

**Breakup Recovery Squad** is built to simulate a *support team*, not a single chatbot.
Each agent plays a distinct psychological role, working together to help users:

* Feel emotionally validated
* Release unspoken thoughts
* Regain structure and routine
* See the situation objectively and move forward

The app is designed with privacy and user control in mind — API keys are stored locally in browser cookies, and no data is persisted on servers.

---

## 🤖 AI Agents Architecture

The system uses a **multi-agent architecture** powered by Google Gemini:

### 1. 🤗 Therapist Agent

* Provides empathetic emotional support
* Analyzes emotional tone from text and uploaded images
* Focuses on validation, comfort, and emotional grounding

### 2. ✍️ Closure Agent

* Helps users express unspoken feelings
* Drafts closure messages that are *not meant to be sent*
* Aims at emotional release rather than reconciliation

### 3. 📅 Recovery Planner Agent

* Designs a personalized **7-day recovery routine**
* Includes self-care, reflection, and light activities
* Encourages rebuilding daily structure

### 4. 💪 Brutal Honesty Agent

* Delivers direct, objective feedback
* Uses factual reasoning to challenge emotional bias
* Helps users detach and regain clarity

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – interactive web UI
* **Google Gemini (gemini-2.5-flash)** – LLM backend
* **Agno Agents Framework** – multi-agent orchestration
* **DuckDuckGo Tools** – factual grounding for honesty agent
* **Browser Cookies** – secure local API key storage

---

## ✨ Key Features

* 🔐 Local API key storage (no backend persistence)
* 🖼️ Optional image input (chat screenshots)
* 🧩 Modular multi-agent design
* ⏳ Rate-limit safe execution flow
* 📱 Clean, user-friendly Streamlit interface

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

You will need a **Google Gemini API Key** from:
[https://aistudio.google.com/](https://aistudio.google.com/)

---

## 🎯 Use Cases

* Emotional processing after breakups
* Journaling with structured AI guidance
* Mental clarity and routine rebuilding
* Demonstration of multi-agent AI systems

---

## 🧩 Project Structure

```
app.py                # Main Streamlit application
```

---

## ⚠️ Disclaimer

This project is **not a replacement for professional mental health care**.
It is intended as a supportive AI tool for reflection and emotional organization.

---

## 👩‍💻 Author

**Esraa Yasser**
Data Scientist & AI Engineer
Focused on applied AI systems, multi-agent architectures, and real-world data-driven solutions.

---

## ⭐ If you like this project

Consider starring ⭐ the repo — feedback and contributions are welcome!

