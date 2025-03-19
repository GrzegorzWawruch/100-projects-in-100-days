import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/8b46a04c9ee6ccedb96b759cd35b4406/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.endpoint = SHEETY_ENDPOINT
        self.authentication = HTTPBasicAuth(self.username, self.password)
        self.destination_data = {}

    def get_sheety_data(self):
        response = requests.get(self.endpoint, auth=self.authentication)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def put_sheety_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                 }
            }
            response = requests.put(url=f"{self.endpoint}/{city["id"]}", auth=self.authentication, json=new_data)
            print(response.text)



