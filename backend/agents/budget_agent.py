def auto_budget_estimation(total_budget, travel_type, days, people):
    """
    Budget Agent:
    Splits total budget into realistic categories and decides hotel category.
    """

    if travel_type == "Budget":
        transport = int(total_budget * 0.25)
        hotel = int(total_budget * 0.30)
        food = int(total_budget * 0.25)
        activities = int(total_budget * 0.10)
        buffer = int(total_budget * 0.10)

    elif travel_type == "Luxury":
        transport = int(total_budget * 0.20)
        hotel = int(total_budget * 0.45)
        food = int(total_budget * 0.20)
        activities = int(total_budget * 0.10)
        buffer = int(total_budget * 0.05)

    elif travel_type == "Adventure":
        transport = int(total_budget * 0.25)
        hotel = int(total_budget * 0.25)
        food = int(total_budget * 0.15)
        activities = int(total_budget * 0.25)
        buffer = int(total_budget * 0.10)

    elif travel_type == "Relaxed":
        transport = int(total_budget * 0.20)
        hotel = int(total_budget * 0.35)
        food = int(total_budget * 0.25)
        activities = int(total_budget * 0.10)
        buffer = int(total_budget * 0.10)

    else:
        transport = int(total_budget * 0.25)
        hotel = int(total_budget * 0.35)
        food = int(total_budget * 0.20)
        activities = int(total_budget * 0.15)
        buffer = int(total_budget * 0.05)

    nights = max(days - 1, 1)
    hotel_per_night_total = int(hotel / nights)
    hotel_per_person_per_night = int(hotel_per_night_total / max(people, 1))
    food_per_person_per_day = int(food / max(days * people, 1))

    if hotel_per_night_total < 700:
        hotel_category = "hostel, dormitory, dharamshala, basic lodge, or shared stay only"
    elif hotel_per_night_total < 1500:
        hotel_category = "budget hotel, guest house, basic homestay, or hostel"
    elif hotel_per_night_total < 3000:
        hotel_category = "2-star hotel, simple 3-star hotel, guest house, or homestay"
    elif hotel_per_night_total < 5000:
        hotel_category = "3-star hotel or selected affordable 4-star hotel only if realistic"
    else:
        hotel_category = "premium 4-star, 5-star, resort, or luxury stay"

    if total_budget < 7000:
        feasibility_note = (
            "Very tight budget. Prefer train/bus travel, hostels, free attractions, "
            "street food, and avoid luxury hotels or expensive activities."
        )
    elif total_budget < 15000:
        feasibility_note = (
            "Moderate-low budget. Choose budget hotels, local food, public transport, "
            "and limited paid activities."
        )
    else:
        feasibility_note = (
            "Budget is workable. Plan can include better hotels, paid attractions, "
            "and comfortable food options."
        )

    return {
        "transport": transport,
        "hotel": hotel,
        "food": food,
        "activities": activities,
        "buffer": buffer,
        "total": transport + hotel + food + activities + buffer,
        "nights": nights,
        "hotel_per_night_total": hotel_per_night_total,
        "hotel_per_person_per_night": hotel_per_person_per_night,
        "food_per_person_per_day": food_per_person_per_day,
        "hotel_category": hotel_category,
        "feasibility_note": feasibility_note
    }