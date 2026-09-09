import sqlite3


DB_NAME = "flight_prices.db"


def init_db():
    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS flight_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price INTEGER NOT NULL,
            airline TEXT NOT NULL,
            departure TEXT NOT NULL,
            arrival TEXT NOT NULL,
            checked_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def save_price(flight):
    connection = sqlite3.connect(DB_NAME)

    connection.execute(
        """
        INSERT INTO flight_prices
        (price, airline, departure, arrival, checked_at)
        VALUES (?, ?, ?, ?, datetime('now'))
        """,
        (
            flight["price"],
            flight["airline"],
            flight["departure"],
            flight["arrival"],
        ),
    )

    connection.commit()
    connection.close()

def get_price_history():
    connection = sqlite3.connect(DB_NAME)

    rows = connection.execute(
        """
        SELECT price, airline, departure, arrival, checked_at
        FROM flight_prices
        ORDER BY checked_at
        """
    ).fetchall()

    connection.close()

    return rows