import streamlit as st


def render_transport_card(transport_suggestion):
    st.markdown("### 🚆 Recommended Transport")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    if transport_suggestion:
        st.write(transport_suggestion)
    else:
        st.write("Transport suggestion not available.")

    st.markdown("</div>", unsafe_allow_html=True)