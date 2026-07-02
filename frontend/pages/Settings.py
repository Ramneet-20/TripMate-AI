import os, sys
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.auth.auth import login_user
from backend.tools.memory_tool import get_user_preferences, update_user_preferences
from frontend.styles import apply_global_styles

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")
apply_global_styles()

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_user()
    st.stop()

username = st.session_state.username
prefs = get_user_preferences(username)

st.title("⚙️ Settings")

food_options = ["Vegetarian", "Non-Vegetarian", "Both"]
travel_options = ["Budget", "Standard", "Luxury", "Adventure", "Relaxed"]

food = st.selectbox(
    "Default Food Preference",
    food_options,
    index=food_options.index(prefs.get("food_preference", "Both"))
)

travel = st.selectbox(
    "Default Travel Type",
    travel_options,
    index=travel_options.index(prefs.get("travel_type", "Standard"))
)

if st.button("Save Settings"):
    update_user_preferences(username, food, travel)
    st.success("Settings saved successfully!")