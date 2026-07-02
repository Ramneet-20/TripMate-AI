import requests
from backend.tools.geoapify_tool import get_coordinates


def get_weather(city):
    try:
        lat, lon = get_coordinates(city)

        if lat is None or lon is None:
            return None

        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "timezone": "auto"
        }

        response = requests.get(url, params=params, timeout=15)
        return response.json()

    except Exception:
        return None