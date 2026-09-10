def parse_flight(flight):
    return {
        "price": flight["price"],
        "airline": flight["flights"][0]["airline"],
        "flight_numbers": [
            segment["flight_number"]
            for segment in flight["flights"]
        ],
        "departure": flight["flights"][0]["departure_airport"]["time"],
        "arrival": flight["flights"][-1]["arrival_airport"]["time"],
        "total_duration": flight["total_duration"],
        "stops": len(flight.get("layovers", [])),
    } 