import os, sys
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.auth.auth import login_user
from backend.tools.memory_tool import get_user_trips, get_user_preferences
from frontend.styles import apply_global_styles

st.set_page_config(page_title="Profile", page_icon="👤", layout="wide")
apply_global_styles()

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_user()
    st.stop()

username = st.session_state.username
trips = get_user_trips(username)
prefs = get_user_preferences(username)

st.title("👤 Profile")

total_budget = sum(int(t.get("budget", 0)) for t in trips)

c1, c2, c3 = st.columns(3)
c1.metric("Username", username)
c2.metric("Trips Created", len(trips))
c3.metric("Total Planned Budget", f"₹{total_budget}")

st.markdown("## Preferences")

st.markdown(f"""
<div class="glass-card">
    <p><b>🍴 Food Preference:</b> {prefs.get("food_preference", "Both")}</p>
    <p><b>🎒 Travel Style:</b> {prefs.get("travel_type", "Standard")}</p>
</div>
""", unsafe_allow_html=True)