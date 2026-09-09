from flight_watcher.search import get_flights
from flight_watcher.filter import (
    filter_by_price,
    filter_by_stops,
    find_cheapest,
)
from flight_watcher.settings import (
    ORIGIN,
    DESTINATION,
    DEPARTURE_DATE,
    RETURN_DATE,
    MAX_PRICE,
    MAX_STOPS,
)


def check_flights():
    flights = get_flights(
        origin=ORIGIN,
        destination=DESTINATION,
        departure_date=DEPARTURE_DATE,
        return_date=RETURN_DATE,
    )

    flights = filter_by_price(flights, max_price=MAX_PRICE)
    flights = filter_by_stops(flights, max_stops=MAX_STOPS)

    return find_cheapest(flights)