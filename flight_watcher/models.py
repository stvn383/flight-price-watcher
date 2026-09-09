from dataclasses import dataclass
from datetime import datetime


@dataclass
class FlightPrice:
    price: int
    airline: str
    departure: str
    arrival: str
    checked_at: datetime