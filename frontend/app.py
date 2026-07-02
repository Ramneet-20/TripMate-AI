import os
import sys
import streamlit as st
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.auth.auth import login_user, logout_user
from backend.agents.budget_agent import auto_budget_estimation
from backend.agents.itinerary_agent import generate_ai_plan, chat_with_tripmate, extract_trip_updates
from backend.agents.transport_agent import suggest_transport
from backend.tools.geoapify_tool import get_places, get_hotels
from backend.tools.weather_tool import get_weather
from backend.tools.news_tool import get_latest_news
from backend.tools.emergency_tool import get_emergency_info
from backend.tools.pdf_tool import create_trip_pdf
from backend.tools.memory_tool import (
    get_user_preferences,
    update_user_preferences,
    get_user_trips,
    save_user_trip
)

from frontend.styles import apply_global_styles
from frontend.components.hero import render_hero
from frontend.components.sidebar import render_sidebar
from frontend.components.budget_card import render_budget_card
from frontend.components.transport_card import render_transport_card
from frontend.components.weather_card import render_weather_card
from frontend.components.place_card import render_place_card
from frontend.components.hotel_card import render_hotel_card
from frontend.components.news_card import render_news_card
from frontend.components.emergency_card import render_emergency_card
from frontend.components.packing_card import render_packing_card
from frontend.components.chat_card import render_chat_card

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

st.set_page_config(page_title="TripMate AI", page_icon="✈️", layout="wide")
apply_global_styles()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in:
    login_user()
    st.stop()

username = st.session_state.username
user_preferences = get_user_preferences(username)
previous_trips = get_user_trips(username)


def generate_packing_checklist(weather, travel_type):
    checklist = [
        "Valid ID proof",
        "Phone charger and power bank",
        "Basic medicines",
        "Comfortable clothes",
        "Comfortable walking shoes",
        "Reusable water bottle",
        "Cash and UPI backup"
    ]

    if weather and "current_weather" in weather:
        temp = weather["current_weather"].get("temperature", 0)

        if temp >= 30:
            checklist.extend(["Sunscreen", "Sunglasses", "Cap or hat", "Light cotton clothes"])

        if temp <= 15:
            checklist.extend(["Warm jacket", "Sweater", "Thermal wear"])

    if weather and "daily" in weather:
        rain_chances = weather["daily"].get("precipitation_probability_max", [])

        if rain_chances and max(rain_chances[:3]) >= 40:
            checklist.extend(["Umbrella", "Raincoat", "Waterproof bag cover"])

    if travel_type == "Adventure":
        checklist.extend(["Trekking shoes", "First-aid kit", "Torch", "Energy bars"])

    return checklist


if "plan" not in st.session_state:
    st.session_state.plan = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "saved_data" not in st.session_state:
    st.session_state.saved_data = {}

render_hero()

trip_inputs = render_sidebar(
    username=username,
    previous_trips=previous_trips,
    user_preferences=user_preferences,
    logout_user=logout_user
)


def create_complete_plan(
    source,
    dest,
    start,
    end,
    total_days,
    total_people,
    selected_travel_type,
    selected_food_preference,
    total_budget
):
    budget_data = auto_budget_estimation(
        total_budget,
        selected_travel_type,
        total_days,
        total_people
    )

    transport_suggestion = suggest_transport(
        source,
        dest,
        total_people,
        selected_travel_type,
        budget_data
    )

    weather = get_weather(dest)
    places = get_places(dest)
    hotels = get_hotels(dest)
    latest_news = get_latest_news(dest)
    emergency_info = get_emergency_info(dest)
    packing_checklist = generate_packing_checklist(weather, selected_travel_type)

    ai_plan = generate_ai_plan(
        source,
        dest,
        start,
        end,
        total_days,
        total_people,
        selected_travel_type,
        total_budget,
        budget_data,
        weather,
        places,
        hotels,
        selected_food_preference,
        latest_news,
        emergency_info,
        packing_checklist,
        transport_suggestion
    )

    return {
        "plan": ai_plan,
        "budget_data": budget_data,
        "transport_suggestion": transport_suggestion,
        "weather": weather,
        "places": places,
        "hotels": hotels,
        "food_preference": selected_food_preference,
        "latest_news": latest_news,
        "emergency_info": emergency_info,
        "packing_checklist": packing_checklist,
        "start_date": start,
        "end_date": end,
        "days": total_days,
        "source_city": source,
        "destination": dest,
        "travel_type": selected_travel_type,
        "budget": total_budget,
        "people": total_people
    }


if trip_inputs["generate_clicked"]:
    source_city = trip_inputs["source_city"]
    destination = trip_inputs["destination"]
    start_date = trip_inputs["start_date"]
    end_date = trip_inputs["end_date"]
    days = trip_inputs["days"]
    people = trip_inputs["people"]
    travel_type = trip_inputs["travel_type"]
    food_preference = trip_inputs["food_preference"]
    budget = trip_inputs["budget"]

    if not GROQ_API_KEY:
        st.error("GROQ_API_KEY is missing. Please check your .env file.")

    elif not GEOAPIFY_API_KEY:
        st.error("GEOAPIFY_API_KEY is missing. Please check your .env file.")

    elif source_city.strip() == "" or destination.strip() == "":
        st.error("Please enter both starting city and destination city.")

    elif start_date is None or end_date is None:
        st.error("Please select both start date and end date.")

    elif end_date < start_date:
        st.error("Trip end date cannot be before start date.")

    elif travel_type == "Select Travel Type":
        st.error("Please select a travel type.")

    elif food_preference == "Select Food Preference":
        st.error("Please select food preference.")

    elif budget <= 0:
        st.error("Please enter a valid budget.")

    else:
        with st.spinner("TripMate AI is planning your trip realistically..."):
            result = create_complete_plan(
                source_city,
                destination,
                start_date,
                end_date,
                days,
                people,
                travel_type,
                food_preference,
                budget
            )

            st.session_state.plan = result["plan"]
            st.session_state.messages = []
            st.session_state.saved_data = result

            update_user_preferences(username, food_preference, travel_type)

            save_user_trip(username, {
                "source": source_city,
                "destination": destination,
                "start_date": str(start_date),
                "end_date": str(end_date),
                "days": days,
                "people": people,
                "travel_type": travel_type,
                "food_preference": food_preference,
                "budget": budget
            })

        st.success("Trip plan generated successfully!")


if st.session_state.plan:
    saved_data = st.session_state.saved_data

    budget_data = saved_data.get("budget_data", {})
    transport_suggestion = saved_data.get("transport_suggestion", "")
    weather = saved_data.get("weather", {})
    places = saved_data.get("places", [])
    hotels = saved_data.get("hotels", [])
    food_preference = saved_data.get("food_preference", "Both")
    latest_news = saved_data.get("latest_news", [])
    emergency_info = saved_data.get("emergency_info", {})
    packing_checklist = saved_data.get("packing_checklist", [])

    saved_start_date = saved_data.get("start_date")
    saved_end_date = saved_data.get("end_date")
    saved_days = saved_data.get("days", 1)
    saved_source = saved_data.get("source_city", "")
    saved_destination = saved_data.get("destination", "")
    saved_travel_type = saved_data.get("travel_type", "")
    saved_budget = saved_data.get("budget", 0)
    saved_people = saved_data.get("people", 1)

    st.markdown("## 🧳 Trip Summary")

    st.success(
        f"You are planning a {saved_days}-day {saved_travel_type.lower()} trip "
        f"from {saved_source} to {saved_destination} from {saved_start_date} to {saved_end_date} "
        f"for {saved_people} person/people within ₹{saved_budget}. "
        f"Food preference: {food_preference}."
    )

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "Overview",
        "Budget",
        "Transport",
        "Weather",
        "Places & Hotels",
        "Safety",
        "AI Plan",
        "Chat"
    ])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### Trip Overview")
        st.write(f"**From:** {saved_source}")
        st.write(f"**To:** {saved_destination}")
        st.write(f"**Dates:** {saved_start_date} to {saved_end_date}")
        st.write(f"**People:** {saved_people}")
        st.write(f"**Budget:** ₹{saved_budget}")
        st.write(f"**Travel Type:** {saved_travel_type}")
        st.write(f"**Food Preference:** {food_preference}")
        st.markdown("</div>", unsafe_allow_html=True)

        render_packing_card(packing_checklist)

    with tab2:
        render_budget_card(budget_data)

    with tab3:
        render_transport_card(transport_suggestion)

    with tab4:
        render_weather_card(weather)

    with tab5:
        col_a, col_b = st.columns(2)

        with col_a:
            render_place_card(places, saved_destination)

        with col_b:
            render_hotel_card(hotels, saved_destination)

    with tab6:
        render_news_card(latest_news)
        render_emergency_card(emergency_info)

    with tab7:
        st.write(st.session_state.plan)

        st.download_button(
            label="Download Trip Plan as Text",
            data=st.session_state.plan,
            file_name="tripmate_ai_plan.txt",
            mime="text/plain"
        )

        try:
            pdf_file = create_trip_pdf(st.session_state.plan)

            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="Download Trip Plan as PDF",
                    data=file,
                    file_name="tripmate_ai_plan.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.warning(f"PDF generation failed: {e}")

    with tab8:
        render_chat_card(
            saved_source=saved_source,
            saved_destination=saved_destination,
            saved_start_date=saved_start_date,
            saved_end_date=saved_end_date,
            saved_days=saved_days,
            saved_people=saved_people,
            saved_travel_type=saved_travel_type,
            food_preference=food_preference,
            saved_budget=saved_budget,
            budget_data=budget_data,
            extract_trip_updates=extract_trip_updates,
            create_complete_plan=create_complete_plan,
            chat_with_tripmate=chat_with_tripmate,
            update_user_preferences=update_user_preferences,
            save_user_trip=save_user_trip,
            username=username
        )