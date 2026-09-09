def average_price(history):
    if not history:
        return None

    prices = [row[0] for row in history]

    return sum(prices) / len(prices)

def lowest_price(history):
    if not history:
        return None

    return min(row[0] for row in history)

def highest_price(history):
    if not history:
        return None

    return max(row[0] for row in history)

def price_change(history):
    if len(history) < 2:
        return None

    first_price = history[0][0]
    latest_price = history[-1][0]

    return latest_price - first_price

def price_change_percent(history):
    if len(history) < 2:
        return None

    first_price = history[0][0]
    latest_price = history[-1][0]

    return ((latest_price - first_price) / first_price) * 100

def price_trend(history):
    if len(history) < 2:
        return "not enough data"

    change = price_change(history)

    if change < 0:
        return "decreasing"
    elif change > 0:
        return "increasing"
    else:
        return "unchanged"

def summarize_history(history):
    return {
        "average": average_price(history),
        "lowest": lowest_price(history),
        "highest": highest_price(history),
        "change": price_change(history),
        "change_percent": price_change_percent(history),
        "trend": price_trend(history),
    }