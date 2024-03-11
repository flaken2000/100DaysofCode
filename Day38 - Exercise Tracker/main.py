import requests
import datetime as dt
import os

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("APP_ID", "Env variable APP_ID doesn't exists")
API_KEY = os.environ.get("API_KEY", "Env variable API_KEY doesn't exists")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Env variable SHEETY_ENDPOINT doesn't exists")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "Env variable SHEETY_TOKEN doesn't exists")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": "80",
    "height_cm": "175",
    "age": "46",
}

response_nutritionix = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
data = response_nutritionix.json()
response_nutritionix.raise_for_status()
date_to_post = dt.datetime.now()

sheety_headers = {
    "Authorization": "Bearer yourtokenhere"

}

for exercise in data["exercises"]:
    sheety_payload = {
        "workout": {
            "date": date_to_post.strftime("%Y-%m-%d"),
            "time": date_to_post.strftime("%H:%M:%S"),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=sheety_payload, headers=sheety_headers)
    response_sheety.raise_for_status()
