# This class is responsible for talking to the Google Sheet.
import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/9d2530d38eefc0961d1c36126922b585/flightDeals/prices"
sheety_header = {"Authorization": "Bearer"}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        sheety_response = requests.get(url=sheety_endpoint, headers=sheety_header)
        data = sheety_response.json()
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata(self):
        for datapoints in self.destination_data:
            sheety_put_params = {
                "price": {
                    "iataCode": datapoints["iataCode"]
                }
            }
            # sheety_endpoint = sheety_endpoint + '/' + datapoints["id"]
            sheety_put_response = requests.put(url=f"{sheety_endpoint}/{datapoints['id']}", json=sheety_put_params, headers=sheety_header)
            # print(sheety_put_response.text)










