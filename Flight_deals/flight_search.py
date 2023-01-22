import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to, date_from, date_to):
        self.endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.api_key = os.environ.get("tequila_api")
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to

    def search(self):
        header = {
            "accept": "application/json",
            "apikey": self.api_key,
        }
        config = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": "INR",
        }
        response = requests.get(url=self.endpoint, headers=header, params=config)
        response.raise_for_status()
        flights = response.json()['data']
        flight_data = []
        for flight in flights:
            price = flight['price']
            departure = flight['local_departure']
            arrival = flight['local_arrival']
            flight_data.append([price, departure, arrival])
        return flight_data


