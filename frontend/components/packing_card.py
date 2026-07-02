import streamlit as st


def render_packing_card(packing_checklist):
    st.markdown("### 🎒 Packing Checklist")

    if packing_checklist:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        for item in packing_checklist:
            st.write(f"✅ {item}")

        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("Packing checklist not available.")