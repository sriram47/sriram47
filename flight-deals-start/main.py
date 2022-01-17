#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta
from notification_manager import NotificationManager

datamanager = DataManager()
flightsearch = FlightSearch()
sheet_data = datamanager.get_destination_data()
notification = NotificationManager()
origin_city = "SFO"

if sheet_data[0]["iataCode"]=="":
    for city in sheet_data:
        city["iataCode"] = flightsearch.iata_code(city["city"])
    datamanager.destination_data = sheet_data
    datamanager.update_iata()


from_time = datetime.strftime((datetime.today() + timedelta(days=1)),"%d/%m/%Y")
to_time = datetime.strftime((datetime.today() + timedelta(days=(6*30))),"%d/%m/%Y")
# flight_data = flightsearch.search_flight(origin_city, "BOM", from_time, to_time)
# print(flight_data)

for city in sheet_data:
    flight_data = flightsearch.search_flight(origin_city, city["iataCode"], from_time, to_time)
    if flight_data.price < city["lowestPrice"]:
        notification.send_email(email_message=f"Only ${flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} from {flight_data.out_date} to {flight_data.return_date}")
