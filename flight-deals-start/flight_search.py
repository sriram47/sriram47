# This class is responsible for talking to the Flight Search API.
import requests
from flight_data import FlightData

API_KEY = ""
base_endpoint = "https://tequila-api.kiwi.com"
iatacode_endpoint = "https://tequila-api.kiwi.com/locations/query"
header = {
        "apikey": API_KEY
}


class FlightSearch:

    def iata_code(self,city_name):
        # iata_code = 'TESTING'
        iatacode_params = {
            "term":city_name
        }
        iatacode_response = requests.get(url=iatacode_endpoint,params=iatacode_params, headers=header)
        data = iatacode_response.json()
        return data["locations"][0]["code"]

    def search_flight(self,from_city, to_city, from_time, to_time):
        flightsearch_endpoint = f"{base_endpoint}/v2/search"
        flight_search_params = {
            "fly_from":from_city,
            "fly_to":to_city,
            "date_from":from_time,
            "date_to":to_time,
            "one_for_city": 1,
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type":"round",
            "max_stopovers":1,
            "curr": "USD"
        }
        flightsearch_response = requests.get(url=flightsearch_endpoint, params=flight_search_params, headers=header)
        # flightsearch_data = flightsearch_response.json()["data"][0]
        try:
            flightsearch_data = flightsearch_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city}.")
            return None

        # flight_data = FlightData(
        #     price=flightsearch_data["price"],
        #     origin_city=flightsearch_data["route"]
        # )

        flight_data = FlightData(
            price=flightsearch_data["price"],
            origin_city=flightsearch_data["route"][0]["cityFrom"],
            origin_airport=flightsearch_data["route"][0]["flyFrom"],
            destination_city=flightsearch_data["route"][0]["cityTo"],
            destination_airport=flightsearch_data["route"][0]["flyTo"],
            out_date=flightsearch_data["route"][0]["local_departure"].split("T")[0],
            return_date=flightsearch_data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data


