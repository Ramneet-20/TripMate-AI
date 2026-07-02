import streamlit as st


def apply_global_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255, 184, 108, 0.28), transparent 35%),
            radial-gradient(circle at top right, rgba(244, 114, 182, 0.20), transparent 30%),
            linear-gradient(135deg, #1c1917 0%, #292524 45%, #0c0a09 100%);
        color: #FFF7ED;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }

    h1 {
        font-size: 58px !important;
        font-weight: 900 !important;
        color: #FFF7ED !important;
        letter-spacing: -1.5px;
    }

    h2, h3, p, label {
        color: #FFF7ED !important;
    }

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, rgba(68, 64, 60, 0.96), rgba(28, 25, 23, 0.98));
        border-right: 1px solid rgba(251, 191, 36, 0.25);
    }

    .hero-card {
        background:
            linear-gradient(135deg, rgba(251, 146, 60, 0.28), rgba(236, 72, 153, 0.20)),
            rgba(28, 25, 23, 0.86);
        padding: 38px;
        border-radius: 30px;
        border: 1px solid rgba(251, 191, 36, 0.35);
        box-shadow: 0 25px 80px rgba(0,0,0,0.35);
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 62px;
        font-weight: 900;
        margin-bottom: 8px;
        background: linear-gradient(90deg, #FDBA74, #F9A8D4, #FDE68A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 21px;
        color: #FED7AA;
        font-weight: 600;
    }

    .glass-card {
        background: rgba(41, 37, 36, 0.88);
        padding: 22px;
        border-radius: 22px;
        border: 1px solid rgba(251, 191, 36, 0.22);
        box-shadow: 0 16px 45px rgba(0,0,0,0.30);
        margin-bottom: 18px;
    }

    .mini-card {
        background:
            linear-gradient(135deg, rgba(251, 146, 60, 0.18), rgba(253, 186, 116, 0.08));
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(251, 191, 36, 0.25);
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.20);
    }

    .mini-card:hover,
    .glass-card:hover {
        transform: translateY(-2px);
        transition: 0.25s ease;
        border-color: rgba(253, 186, 116, 0.65);
    }

    .stMetric {
        background: rgba(41, 37, 36, 0.92);
        padding: 18px;
        border-radius: 18px;
        border: 1px solid rgba(251, 191, 36, 0.25);
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    .stButton button {
        border-radius: 14px;
        background: linear-gradient(90deg, #F97316, #EC4899);
        color: white;
        border: none;
        padding: 0.7rem 1.1rem;
        font-weight: 800;
        box-shadow: 0 10px 28px rgba(249, 115, 22, 0.25);
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #EA580C, #DB2777);
        color: white;
        transform: translateY(-1px);
        transition: 0.2s ease;
    }

    .stTextInput input,
    .stNumberInput input,
    .stDateInput input {
        border-radius: 14px !important;
        border: 1px solid rgba(251, 191, 36, 0.28) !important;
        background-color: rgba(68, 64, 60, 0.9) !important;
        color: #FFF7ED !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        border-radius: 14px !important;
        background-color: rgba(68, 64, 60, 0.9) !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 16px;
        border: 1px solid rgba(251, 191, 36, 0.22);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(68, 64, 60, 0.70);
        border-radius: 14px;
        padding: 10px 18px;
        color: #FED7AA;
        border: 1px solid rgba(251, 191, 36, 0.20);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #F97316, #EC4899) !important;
        color: white !important;
    }

    a {
        color: #FDBA74 !important;
        font-weight: 700;
        text-decoration: none;
    }

    a:hover {
        color: #F9A8D4 !important;
        text-decoration: underline;
    }

    hr {
        border-color: rgba(251, 191, 36, 0.20);
    }
    </style>
    """, unsafe_allow_html=True)