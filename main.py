from func_messaging import send_message
from func_owm_get import get_weather_forecast

will_rain = False

for condition in get_weather_forecast():
    if condition < 700:
        will_rain = True

if will_rain:
    send_message("Its going to be rainy today, bring an umbrella!")