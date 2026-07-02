import streamlit as st


def render_hotel_card(hotels, destination=""):
    st.markdown("### 🏨 Recommended Hotels")

    if hotels:
        for hotel in hotels:
            name = hotel.get("name", "Unnamed Hotel")
            address = hotel.get("address", "Address not available")

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)

            st.write(f"#### 🏨 {name}")
            st.caption(address)

            st.write("💰 Price: Check live price before booking")
            st.write("⭐ Category: Budget / Standard depending on availability")
            st.write("🛏️ Tip: Compare prices on MakeMyTrip, Goibibo, Booking.com before booking.")

            if hotel.get("maps_link"):
                st.markdown(f"[🗺️ Open in Google Maps]({hotel['maps_link']})")

            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No hotels found.")