from flight_watcher.flight_api import search_flights
from flight_watcher.parser import parse_flight


def get_flights(origin, destination, departure_date, return_date):
    results = search_flights(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        return_date=return_date,
    )

    flights = results.get("best_flights", [])

    return [parse_flight(flight) for flight in flights]