import os, sys
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.auth.auth import login_user
from backend.tools.memory_tool import get_user_trips
from frontend.styles import apply_global_styles

st.set_page_config(page_title="My Trips", page_icon="🧳", layout="wide")
apply_global_styles()

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_user()
    st.stop()

username = st.session_state.username
trips = get_user_trips(username)

st.title("🧳 My Trips")

if trips:
    for i, trip in enumerate(trips[::-1], 1):
        st.markdown(f"""
        <div class="glass-card">
            <h3>{i}. {trip.get('source')} → {trip.get('destination')}</h3>
            <p><b>Dates:</b> {trip.get('start_date')} to {trip.get('end_date')}</p>
            <p><b>Days:</b> {trip.get('days')}</p>
            <p><b>People:</b> {trip.get('people')}</p>
            <p><b>Budget:</b> ₹{trip.get('budget')}</p>
            <p><b>Travel Type:</b> {trip.get('travel_type')}</p>
            <p><b>Food:</b> {trip.get('food_preference')}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No saved trips yet.")