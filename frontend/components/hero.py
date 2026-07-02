import streamlit as st


def render_hero():
    st.markdown("""
    <div class="hero-card">
        <div class="hero-title">🌍 TripMate AI</div>
        <div class="hero-subtitle">
            Plan smarter. Travel safer. Stay within budget.
        </div>
        <br>
        <p>
            Your personalized AI travel assistant for budget planning, transport suggestions,
            hotel recommendations, weather alerts, emergency info, packing checklist, and trip chat.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown('<div class="mini-card">📍<br><b>Destination</b><br>Smart planning</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="mini-card">💰<br><b>Budget</b><br>Realistic split</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="mini-card">🚆<br><b>Transport</b><br>Budget fit</div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="mini-card">💬<br><b>AI Chat</b><br>Modify plans</div>', unsafe_allow_html=True)