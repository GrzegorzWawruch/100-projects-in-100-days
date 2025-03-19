
from data_manager import *
from flight_search import *
from flight_data import *
from pprint import pprint
import time
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheety_data()

ORIGIN_CITY_IATA = "WAR"

for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_destination_code(city["city"])


pprint(sheet_data)



sheet_data = data_manager.put_sheety_data()

# data = flight_search.get_destination_code("PARIS")
# pprint(data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)