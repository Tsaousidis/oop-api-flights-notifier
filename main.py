
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# Create objects for data management, flight search, and sending notifications
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "SKG" # Set the origin airport (Thessaloniki)

# Update IATA codes for each destination if they are missing
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

# Update the destination data in Sheety API with the IATA codes
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# Set up the dates for flight search (tomorrow and 6 months from today)
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Search for the cheapest flights to each destination
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    time.sleep(2)

    # If a cheaper flight is found, send a notification
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        
        # Create and send the notification message
        subject = "✈️ Low Price Flight Alert!"
        message = (
            f"Low price alert! Only £{cheapest_flight.price} to fly from "
            f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        try:
            notification_manager.send_email(subject, message) # Send email notification
        except Exception as e:
            print(f"❌ Failed to send email for {destination['city']}: {e}") # Print error if email fails to send
