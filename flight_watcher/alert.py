def format_alert(flight):
    if flight is None:
        return "No flights matched your criteria."

    return (
        f"Flight found: ${flight['price']} | "
        f"{flight['airline']} | "
        f"{flight['flight_numbers']} | "
        f"{flight['stops']} stop(s)"
    )