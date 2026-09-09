from flight_watcher.database import get_price_history
from flight_watcher.analysis import summarize_history
from flight_watcher.analysis import median_price

history = get_price_history()

summary = summarize_history(history, "2026-12-18")
median = median_price(history)
print("Flight Price Summary")
print("--------------------")
print(f"Average: ${summary['average']:.2f}")
print(f"Median: ${summary['median']:.2f}")
print(f"Lowest: ${summary['lowest']:.2f}")
print(f"Highest: ${summary['highest']:.2f}")
print(f"Change: ${summary['change']:.2f}")
print(f"Change %: {summary['change_percent']:.2f}%")
print(f"Trend: {summary['trend']}")

from flight_watcher.analysis import days_until_departure

days = days_until_departure("2026-12-18")
print(f"Days until departure: {days}")

print(f"Days Until Departure: {summary['days_until_departure']}")