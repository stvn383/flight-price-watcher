from flight_watcher.database import get_price_history
from flight_watcher.analysis import average_price
from flight_watcher.analysis import highest_price
from flight_watcher.analysis import price_change
from flight_watcher.analysis import price_change_percent
from flight_watcher.analysis import price_trend

history = get_price_history()

change = price_change(history)
average = average_price(history)
highest = highest_price(history)
percent = price_change_percent(history)
trend = price_trend(history)

print(f"Highest price: ${highest:.2f}")
print(f"Average price: ${average:.2f}")
print(f"Price change: {change}, Percent: {percent}")
print(f"Price trend: {trend}")