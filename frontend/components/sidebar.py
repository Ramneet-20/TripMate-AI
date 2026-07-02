import streamlit as st


def render_sidebar(username, previous_trips, user_preferences, logout_user):
    st.sidebar.success(f"Logged in as: {username}")
    logout_user()

    st.sidebar.markdown("### 🧳 Previous Trips")

    if previous_trips:
        for trip in previous_trips[-3:]:
            st.sidebar.write(
                f"{trip.get('source', '')} → {trip.get('destination', '')} | ₹{trip.get('budget', '')}"
            )
    else:
        st.sidebar.write("No previous trips yet.")

    st.sidebar.markdown("---")
    st.sidebar.header("Plan Your Trip")

    source_city = st.sidebar.text_input(
        "Starting City",
        value="",
        placeholder="Example: Jaipur"
    )

    destination = st.sidebar.text_input(
        "Destination City",
        value="",
        placeholder="Example: Goa"
    )

    start_date = st.sidebar.date_input("Trip Start Date", value=None)
    end_date = st.sidebar.date_input("Trip End Date", value=None)

    if start_date and end_date:
        days = (end_date - start_date).days + 1

        if days <= 0:
            st.sidebar.error("End date should be after or same as start date.")
            days = 1

        st.sidebar.info(f"Trip Duration: {days} day(s)")
    else:
        days = 1
        st.sidebar.info("Select trip dates to calculate duration.")

    people = st.sidebar.number_input(
        "Number of People",
        min_value=1,
        max_value=20,
        value=1
    )

    travel_options = ["Select Travel Type", "Budget", "Standard", "Luxury", "Adventure", "Relaxed"]
    default_travel = user_preferences.get("travel_type", "Standard")

    travel_type = st.sidebar.selectbox(
        "Travel Type",
        travel_options,
        index=travel_options.index(default_travel) if default_travel in travel_options else 0
    )

    food_options = ["Select Food Preference", "Vegetarian", "Non-Vegetarian", "Both"]
    default_food = user_preferences.get("food_preference", "Both")

    food_preference = st.sidebar.selectbox(
        "Food Preference",
        food_options,
        index=food_options.index(default_food) if default_food in food_options else 0
    )

    budget = st.sidebar.number_input(
        "Total Budget ₹",
        min_value=0,
        value=0
    )

    generate_clicked = st.sidebar.button("🚀 Generate Complete Trip Plan")

    return {
        "source_city": source_city,
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "days": days,
        "people": people,
        "travel_type": travel_type,
        "food_preference": food_preference,
        "budget": budget,
        "generate_clicked": generate_clicked
    }