from flight_watcher.database import get_price_history
from flight_watcher.analysis import (
    summarize_history,
    price_vs_average,
)
from flight_watcher.settings import DEPARTURE_DATE


history = get_price_history()

print("Flight Price Summary")
print("--------------------")

if not history:
    print("No price history available.")
else:
    summary = summarize_history(history, DEPARTURE_DATE)
    current_price = history[-1][0]

    print(f"Current Price: ${current_price:.2f}")
    print(f"Average: ${summary['average']:.2f}")
    print(f"Median: ${summary['median']:.2f}")
    print(f"Lowest: ${summary['lowest']:.2f}")
    print(f"Highest: ${summary['highest']:.2f}")
    print(f"Price Range: ${summary['price_range']:.2f}")
    print(f"Change: ${summary['change']:.2f}")
    print(f"Change %: {summary['change_percent']:.2f}%")
    print(f"Trend: {summary['trend']}")
    print(f"Days Until Departure: {summary['days_until_departure']}")

    difference = price_vs_average(history, current_price)
    print(f"Current vs Average: ${difference:.2f}")