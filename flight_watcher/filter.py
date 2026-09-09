def filter_by_price(flights, max_price):
    return [
        flight
        for flight in flights
        if flight["price"] <= max_price
    ]

def filter_by_stops(flights, max_stops):
    return [
        flight
        for flight in flights
        if flight["stops"] <= max_stops
    ]

def find_cheapest(flights):
    if not flights:
        return None

    return min(flights, key=lambda flight: flight["price"])