from constants import WEATHER_PARAMS, OWM_ENDPOINT
import requests

def get_weather_forecast() -> list:
    response = requests.get(OWM_ENDPOINT, params=WEATHER_PARAMS)
    response.raise_for_status()
    weather_data = response.json()
    weather_condition_ids = []

    for hour_data in weather_data["list"]:
        weather_condition_ids.append(hour_data["weather"][0]["id"])

    return weather_condition_ids