
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


class DataManager:
    """Responsible for interacting with Sheety API to manage destination data."""
    def __init__(self):
        # Initialize the DataManager with user credentials for authentication
        self._user = os.getenv("SHEETY_USRERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        """Fetches destination data from the Sheety API."""
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Updates the IATA codes for the destinations in the Sheety database."""
        for city in self.destination_data:
            new_data = {
                "price": {"iataCode": city["iataCode"]}
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
        