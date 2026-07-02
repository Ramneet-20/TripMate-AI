import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")


def get_coordinates(city):
    try:
        url = "https://api.geoapify.com/v1/geocode/search"

        params = {
            "text": city,
            "apiKey": GEOAPIFY_API_KEY
        }

        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        if data.get("features"):
            lon, lat = data["features"][0]["geometry"]["coordinates"]
            return lat, lon

        return None, None

    except Exception:
        return None, None


def get_places(city):
    try:
        lat, lon = get_coordinates(city)

        if lat is None or lon is None:
            return []

        url = "https://api.geoapify.com/v2/places"

        params = {
            "categories": "tourism.sights,tourism.attraction,entertainment,leisure",
            "filter": f"circle:{lon},{lat},12000",
            "bias": f"proximity:{lon},{lat}",
            "limit": 8,
            "apiKey": GEOAPIFY_API_KEY
        }

        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        places = []

        for item in data.get("features", []):
            prop = item.get("properties", {})
            name = prop.get("name")

            if name:
                places.append({
                    "name": name,
                    "address": prop.get("formatted", "Address not available"),
                    "maps_link": f"https://www.google.com/maps/search/?api=1&query={name.replace(' ', '+')}+{city.replace(' ', '+')}"
                })

        return places

    except Exception:
        return []


def get_hotels(city):
    try:
        lat, lon = get_coordinates(city)

        if lat is None or lon is None:
            return []

        url = "https://api.geoapify.com/v2/places"

        params = {
            "categories": "accommodation.hotel",
            "filter": f"circle:{lon},{lat},12000",
            "bias": f"proximity:{lon},{lat}",
            "limit": 8,
            "apiKey": GEOAPIFY_API_KEY
        }

        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        hotels = []

        for item in data.get("features", []):
            prop = item.get("properties", {})
            name = prop.get("name")

            if name:
                hotels.append({
                    "name": name,
                    "address": prop.get("formatted", "Address not available"),
                    "maps_link": f"https://www.google.com/maps/search/?api=1&query={name.replace(' ', '+')}+{city.replace(' ', '+')}"
                })

        return hotels

    except Exception:
        return []