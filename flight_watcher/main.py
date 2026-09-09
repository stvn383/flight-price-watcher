from flight_watcher.watcher import check_flights
from flight_watcher.alert import format_alert
from flight_watcher.database import init_db
from flight_watcher.database import init_db, save_price

def main():
    init_db()

    flight = check_flights()
    if flight:
        save_price(flight)
    message = format_alert(flight)

    print(message)


if __name__ == "__main__":
    main()