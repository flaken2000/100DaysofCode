from pprint import pprint
import requests
import os
SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT", "Env variable SHEETY_PRICES_ENDPOINT doesn't exists")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT", "Env variable SHEETY_USERS_ENDPOINT doesn't exists")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "Env variable SHEETY_TOKEN doesn't exists")
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint,headers=SHEETY_HEADERS)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
