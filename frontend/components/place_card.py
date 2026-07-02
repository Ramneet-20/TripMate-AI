import streamlit as st


def render_place_card(places, destination=""):
    st.markdown("### 📍 Tourist Places")

    if places:
        for place in places:
            name = place.get("name", "Unnamed Place")
            address = place.get("address", "Address not available")

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)

            st.write(f"#### 📍 {name}")
            st.caption(address)

            st.write("💸 Approx Cost: Budget-friendly / varies by activity")
            st.write("🕒 Suggested Time: 1–2 hours")
            st.write("⭐ Travel Tip: Visit during morning or evening for a better experience.")

            if place.get("maps_link"):
                st.markdown(f"[🗺️ Open in Google Maps]({place['maps_link']})")

            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No places found.")