import streamlit as st


def render_emergency_card(emergency_info):
    st.markdown("### 🚨 Emergency Contact Information")

    if emergency_info:
        e1, e2, e3, e4 = st.columns(4)

        e1.metric("Emergency", emergency_info.get("national_emergency", "112"))
        e2.metric("Police", emergency_info.get("police", "100"))
        e3.metric("Ambulance", emergency_info.get("ambulance", "108"))
        e4.metric("Fire", emergency_info.get("fire", "101"))

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write(f"Tourist Helpline: **{emergency_info.get('tourist_helpline', '1363')}**")
        st.write(f"Women Helpline: **{emergency_info.get('women_helpline', '1091')}**")
        st.write(f"Child Helpline: **{emergency_info.get('child_helpline', '1098')}**")
        st.caption(
            emergency_info.get(
                "note",
                "Keep local emergency numbers and nearest hospital location saved."
            )
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("Emergency information not available.")