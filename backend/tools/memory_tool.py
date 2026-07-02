import json
import os

USERS_FILE = "data/users.json"
TRIPS_FILE = "data/trips.json"


def load_json(file_path):
    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r") as file:
        return json.load(file)


def save_json(file_path, data):
    os.makedirs("data", exist_ok=True)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def get_user_preferences(username):
    users = load_json(USERS_FILE)
    user = users.get(username, {})

    return {
        "food_preference": user.get("food_preference", "Both"),
        "travel_type": user.get("travel_type", "Standard")
    }


def update_user_preferences(username, food_preference, travel_type):
    users = load_json(USERS_FILE)

    if username in users:
        users[username]["food_preference"] = food_preference
        users[username]["travel_type"] = travel_type

    save_json(USERS_FILE, users)


def get_user_trips(username):
    trips = load_json(TRIPS_FILE)
    return trips.get(username, [])


def save_user_trip(username, trip_data):
    trips = load_json(TRIPS_FILE)

    if username not in trips:
        trips[username] = []

    trips[username].append(trip_data)

    save_json(TRIPS_FILE, trips)