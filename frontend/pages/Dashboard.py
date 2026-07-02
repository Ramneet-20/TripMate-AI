import os, sys
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.auth.auth import login_user
from backend.tools.memory_tool import get_user_trips, get_user_preferences
from frontend.styles import apply_global_styles

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
apply_global_styles()

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_user()
    st.stop()

username = st.session_state.username
trips = get_user_trips(username)
prefs = get_user_preferences(username)

st.title("📊 TripMate Dashboard")
st.write(f"Welcome back, **{username}** 👋")

c1, c2, c3 = st.columns(3)
c1.metric("Trips Planned", len(trips))
c2.metric("Preferred Food", prefs.get("food_preference", "Both"))
c3.metric("Travel Style", prefs.get("travel_type", "Standard"))

st.markdown("## Recent Trips")

if trips:
    for trip in trips[-5:][::-1]:
        st.markdown(f"""
        <div class="glass-card">
            <h3>🌍 {trip.get('source')} → {trip.get('destination')}</h3>
            <p>📅 {trip.get('start_date')} to {trip.get('end_date')}</p>
            <p>💰 Budget: ₹{trip.get('budget')}</p>
            <p>🍴 Food: {trip.get('food_preference')}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No trips planned yet. Go to TripMate AI page and create your first trip.")