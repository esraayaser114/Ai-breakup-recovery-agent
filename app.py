import streamlit as st
import extra_streamlit_components as stx
from agno.agent import Agent
from agno.models.google import Gemini
from agno.media import Image as AgnoImage
from agno.tools.duckduckgo import DuckDuckGoTools
from typing import List, Optional
import logging
import os
import time
import datetime

# --- Configuration ---
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# --- Agent Initialization ---

@st.cache_resource
def initialize_agents(api_key: str) -> Optional[tuple[Agent, Agent, Agent, Agent]]:
    try:
        # Use gemini-1.5-flash for best speed and free-tier stability
        model = Gemini(id="gemini-2.5-flash", api_key=api_key)

        # 1. Therapist Agent
        therapist_agent = Agent(
            model=model,
            name="Therapist Agent",
            instructions=[
                "You are an empathetic therapist.",
                "Listen with empathy, validate feelings, and offer comforting words.",
                "Analyze text and images for emotional context."
            ],
            markdown=True
        )

        # 2. Closure Agent
        closure_agent = Agent(
            model=model,
            name="Closure Agent",
            instructions=[
                "You are a closure specialist.",
                "Draft emotional messages for unsent feelings.",
                "Focus on emotional release."
            ],
            markdown=True
        )

        # 3. Routine Planner Agent
        routine_planner_agent = Agent(
            model=model,
            name="Routine Planner Agent",
            instructions=[
                "You are a recovery routine planner.",
                "Design a 7-day recovery challenge.",
                "Suggest fun activities and self-care."
            ],
            markdown=True
        )

        # 4. Brutal Honesty Agent
        brutal_honesty_agent = Agent(
            model=model,
            name="Brutal Honesty Agent",
            tools=[DuckDuckGoTools()], 
            instructions=[
                "You are a direct feedback specialist.",
                "Give raw, objective, and blunt feedback about the breakup.",
                "Provide factual reasons to move forward."
            ],
            markdown=True
        )

        return therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent

    except Exception as e:
        st.error(f"Error initializing agents: {str(e)}")
        return None

# --- Main Application Logic ---

def run_recovery_plan(user_input: str, uploaded_files: List):
    agents = st.session_state.get("agents")
    if not agents:
        st.error("Agents are not initialized. Please check API Key.")
        return

    therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent = agents

    st.header("Your Personalized Recovery Plan 🛡️")

    # Prepare images
    all_images = []
    if uploaded_files:
        for file in uploaded_files:
            file.seek(0)
            all_images.append(AgnoImage(content=file.getvalue()))

    # 1. Therapist Analysis
    try:
        with st.spinner("🤗 Getting empathetic support..."):
            therapist_prompt = f"Analyze the emotional state: {user_input}"
            response = therapist_agent.run(therapist_prompt, images=all_images)
            st.subheader("🤗 Emotional Support")
            st.markdown(response.content)
            time.sleep(2) # Prevent Rate Limit
    except Exception as e:
        st.error(f"Therapist Agent failed: {e}")

    # 2. Closure Messages
    try:
        with st.spinner("✍️ Crafting closure messages..."):
            closure_prompt = f"Draft closure messages for: {user_input}"
            response = closure_agent.run(closure_prompt, images=all_images)
            st.subheader("✍️ Finding Closure")
            st.markdown(response.content)
            time.sleep(2)
    except Exception as e:
        st.error(f"Closure Agent failed: {e}")

    # 3. Recovery Plan
    try:
        with st.spinner("📅 Creating your routine..."):
            routine_prompt = f"Design a 7-day recovery plan for: {user_input}"
            response = routine_planner_agent.run(routine_prompt, images=all_images)
            st.subheader("📅 Your Recovery Plan")
            st.markdown(response.content)
            time.sleep(2)
    except Exception as e:
        st.error(f"Routine Agent failed: {e}")

    # 4. Honest Feedback
    try:
        with st.spinner("💪 Getting real with you..."):
            honesty_prompt = f"Give brutal honest feedback: {user_input}"
            response = brutal_honesty_agent.run(honesty_prompt, images=all_images)
            st.subheader("💪 Honest Perspective")
            st.markdown(response.content)
    except Exception as e:
        st.error(f"Honesty Agent failed: {e}")

# --- Streamlit UI ---

st.set_page_config(page_title="💔 Breakup Recovery Squad", page_icon="💔", layout="wide")

# 1. Setup Cookie Manager (Direct initialization, NO @cache decorator)
cookie_manager = stx.CookieManager(key="recovery_cookie_manager")

# 2. Attempt to fetch existing key from cookies
# Note: .get() can trigger a re-run internally if the component is syncing
cookie_api_key = cookie_manager.get(cookie="gemini_api_key_v1")

with st.sidebar:
    st.header("🔑 API Configuration")
    
    # Determine initial value for text input
    default_val = cookie_api_key if cookie_api_key else os.environ.get("GEMINI_API_KEY", "")
    
    api_key_input = st.text_input(
        "Enter Gemini API Key",
        value=default_val,
        type="password",
        help="Get key from https://aistudio.google.com/"
    )

    # Save button to persist the cookie
    if st.button("Save Key for Later 💾"):
        if api_key_input:
            # Save to browser cookie (Expires in 30 days)
            cookie_manager.set("gemini_api_key_v1", api_key_input, expires_at=datetime.datetime.now() + datetime.timedelta(days=30))
            st.success("Key saved to browser! 🍪")
            time.sleep(0.5)
            st.rerun() # Reload to apply
        else:
            st.warning("Please enter a key first.")
    
    # Clear button
    if st.button("Clear Saved Key 🗑️"):
        cookie_manager.delete("gemini_api_key_v1")
        st.rerun()

    # --- Init Logic ---
    final_api_key = api_key_input

    if final_api_key:
        st.success("System Ready ✅")
        # Initialize agents if new key or not loaded
        if "agents" not in st.session_state or st.session_state.get("last_key") != final_api_key:
            with st.spinner("Initializing agents..."):
                st.session_state.agents = initialize_agents(final_api_key)
                st.session_state.last_key = final_api_key
    else:
        st.warning("API Key required.")

st.title("💔 Breakup Recovery Squad")
st.markdown("### Your AI support team is here.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Share Your Feelings")
    user_input = st.text_area("What happened?", height=150, placeholder="I miss them...")

with col2:
    st.subheader("Chat Screenshots (Optional)")
    uploaded_files = st.file_uploader("Upload chat logs", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

is_ready = final_api_key and (user_input or uploaded_files)

if st.button("Get Recovery Plan 💝", type="primary", disabled=not is_ready):
    run_recovery_plan(user_input, uploaded_files)
elif not final_api_key:
    st.info("Please enter your API Key in the sidebar to start.")