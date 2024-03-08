#
# Day 35 challenge is using OpenWeather API it now can take hours for the API key to be activated.
# Additionally, after creating a Twilio account my account was flagged for review and suspended.
# I have included the final code as provided by the course, but I did not write this code. I only watched the videos.
#
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "__YOUR_OWM_API_KEY__"
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="YOUR TWILIO VIRTUAL NUMBER",
            to="YOUR TWILIO VERIFIED REAL NUMBER"
        )
    print(message.status)
