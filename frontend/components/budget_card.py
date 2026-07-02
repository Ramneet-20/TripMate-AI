import streamlit as st


def render_budget_card(budget_data):
    st.markdown("### 💰 Budget Breakdown")

    b1, b2, b3, b4, b5 = st.columns(5)

    b1.metric("Transport", f"₹{budget_data.get('transport', 0)}")
    b2.metric("Hotel", f"₹{budget_data.get('hotel', 0)}")
    b3.metric("Food", f"₹{budget_data.get('food', 0)}")
    b4.metric("Activities", f"₹{budget_data.get('activities', 0)}")
    b5.metric("Buffer", f"₹{budget_data.get('buffer', 0)}")

    total = max(budget_data.get("total", 1), 1)

    st.write("#### Budget Allocation")

    for label, key in [
        ("Transport", "transport"),
        ("Hotel", "hotel"),
        ("Food", "food"),
        ("Activities", "activities"),
        ("Buffer", "buffer")
    ]:
        amount = budget_data.get(key, 0)
        percent = amount / total
        st.write(f"{label}: ₹{amount}")
        st.progress(percent)

    st.info(
        f"Hotel/night: ₹{budget_data.get('hotel_per_night_total', 0)} | "
        f"Food/person/day: ₹{budget_data.get('food_per_person_per_day', 0)} | "
        f"Allowed stay: {budget_data.get('hotel_category', 'N/A')}"
    )

    if budget_data.get("feasibility_note"):
        st.warning(budget_data.get("feasibility_note"))