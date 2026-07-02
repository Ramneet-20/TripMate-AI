import os, sys
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.auth.auth import login_user
from backend.tools.groq_tool import call_groq
from backend.tools.memory_tool import get_user_trips, get_user_preferences
from frontend.styles import apply_global_styles

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="wide")
apply_global_styles()

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_user()
    st.stop()

username = st.session_state.username
trips = get_user_trips(username)
prefs = get_user_preferences(username)

st.title("🤖 TripMate AI Assistant")
st.write("Ask general travel questions based on your preferences and previous trips.")

if "assistant_messages" not in st.session_state:
    st.session_state.assistant_messages = []

for msg in st.session_state.assistant_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask TripMate anything...")

if question:
    st.session_state.assistant_messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.write(question)

    prompt = f"""
You are TripMate AI assistant.

User: {username}
Preferences: {prefs}
Previous trips: {trips[-5:]}

Question:
{question}

Answer practically and clearly.
"""

    answer = call_groq(prompt)

    st.session_state.assistant_messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)