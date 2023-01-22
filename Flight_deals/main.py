from data_manager import get_data, save_data
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
print(get_data())
fly_from = input("Where you want to start your journey(IATA code): ").upper()
fly_to = input("Where you want to go(IATA code): ").upper()

curr_date = datetime.now().strftime("%d/%m/%Y")
after_30days = (datetime.now()+timedelta(days=30)).strftime("%d/%m/%Y")

flight = FlightSearch(fly_from=fly_from, fly_to=fly_to, date_from=curr_date, date_to=after_30days)
flight_data = flight.search()

save_data(flight_data)

notify = NotificationManager(flight_data[0])
