import streamlit as st


def render_chat_card(
    saved_source,
    saved_destination,
    saved_start_date,
    saved_end_date,
    saved_days,
    saved_people,
    saved_travel_type,
    food_preference,
    saved_budget,
    budget_data,
    extract_trip_updates,
    create_complete_plan,
    chat_with_tripmate,
    update_user_preferences,
    save_user_trip,
    username
):
    st.markdown("### 💬 Chat with TripMate AI")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_question = st.chat_input("Ask anything about your trip...")

    if user_question:
        st.session_state.messages.append({
            "role": "user",
            "content": user_question
        })

        with st.chat_message("user"):
            st.write(user_question)

        current_trip_data = {
            "source_city": saved_source,
            "destination": saved_destination,
            "start_date": str(saved_start_date),
            "end_date": str(saved_end_date),
            "days": saved_days,
            "people": saved_people,
            "travel_type": saved_travel_type,
            "food_preference": food_preference,
            "budget": saved_budget
        }

        updates = extract_trip_updates(user_question, current_trip_data)

        if updates:
            with st.spinner("Updating your trip plan..."):
                new_source = updates.get("source_city", saved_source)
                new_destination = updates.get("destination", saved_destination)
                new_budget = int(updates.get("budget", saved_budget))
                new_people = int(updates.get("people", saved_people))
                new_travel_type = updates.get("travel_type", saved_travel_type)
                new_food_preference = updates.get("food_preference", food_preference)

                result = create_complete_plan(
                    new_source,
                    new_destination,
                    saved_start_date,
                    saved_end_date,
                    saved_days,
                    new_people,
                    new_travel_type,
                    new_food_preference,
                    new_budget
                )

                st.session_state.plan = result["plan"]
                st.session_state.saved_data = result

                update_user_preferences(username, new_food_preference, new_travel_type)

                save_user_trip(username, {
                    "source": new_source,
                    "destination": new_destination,
                    "start_date": str(saved_start_date),
                    "end_date": str(saved_end_date),
                    "days": saved_days,
                    "people": new_people,
                    "travel_type": new_travel_type,
                    "food_preference": new_food_preference,
                    "budget": new_budget
                })

                answer = (
                    f"Updated your trip plan successfully for {new_destination} "
                    f"with budget ₹{new_budget}."
                )

        else:
            with st.spinner("TripMate AI is thinking..."):
                answer = chat_with_tripmate(
                    user_question,
                    st.session_state.plan,
                    budget_data,
                    food_preference
                )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)

        st.rerun()