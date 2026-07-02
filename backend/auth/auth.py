import json
import os
import streamlit as st

USERS_FILE = "data/users.json"


def apply_auth_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827);
    }

    .block-container {
        padding-top: 3rem;
        max-width: 900px;
    }

    h1, h2, h3, p, label {
        color: #F9FAFB !important;
    }

    .auth-card {
        background: rgba(17, 24, 39, 0.92);
        padding: 35px;
        border-radius: 24px;
        border: 1px solid #334155;
        box-shadow: 0px 20px 60px rgba(0,0,0,0.35);
        text-align: center;
        margin-bottom: 25px;
    }

    .auth-title {
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .auth-subtitle {
        font-size: 18px;
        color: #CBD5E1 !important;
        margin-bottom: 20px;
    }

    .feature-box {
        background: rgba(30, 41, 59, 0.8);
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #334155;
        text-align: center;
    }

    .stTextInput input {
        border-radius: 12px !important;
        padding: 12px !important;
    }

    .stButton button {
        border-radius: 12px;
        background: linear-gradient(90deg, #2563EB, #7C3AED);
        color: white;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 700;
        width: 100%;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #1D4ED8, #6D28D9);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    os.makedirs("data", exist_ok=True)

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def signup_user():
    st.markdown("### 📝 Create your account")

    username = st.text_input("Create Username", key="signup_username")
    password = st.text_input("Create Password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

    if st.button("Create Account"):
        users = load_users()

        if username.strip() == "" or password.strip() == "":
            st.error("Username and password cannot be empty.")

        elif username in users:
            st.error("Username already exists. Please login.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        else:
            users[username] = {
                "password": password,
                "food_preference": "Both",
                "travel_type": "Standard"
            }

            save_users(users)
            st.success("Account created successfully! Please login now.")


def login_user():
    apply_auth_css()

    st.markdown("""
    <div class="auth-card">
        <div class="auth-title">🌍 TripMate AI</div>
        <div class="auth-subtitle">
            Plan smarter, travel safer, and stay within budget.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="feature-box">💰<br><b>Budget Planning</b></div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="feature-box">🌦️<br><b>Weather Alerts</b></div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="feature-box">🤖<br><b>AI Itinerary</b></div>', unsafe_allow_html=True)

    st.write("")

    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])

    with tab1:
        st.markdown("### Welcome back 👋")

        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            users = load_users()

            if username in users and users[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        signup_user()


def logout_user():
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()