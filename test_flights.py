from flight_watcher.database import get_price_history
from flight_watcher.analysis import summarize_history

history = get_price_history()

summary = summarize_history(history)

print("Flight Price Summary")
print("--------------------")
print(f"Average: ${summary['average']:.2f}")
print(f"Lowest: ${summary['lowest']:.2f}")
print(f"Highest: ${summary['highest']:.2f}")
print(f"Change: ${summary['change']:.2f}")
print(f"Change %: {summary['change_percent']:.2f}%")
print(f"Trend: {summary['trend']}")