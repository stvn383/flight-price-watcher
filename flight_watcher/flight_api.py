import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FLIGHT_API_KEY")

def search_flights(origin, destination, departure_date, return_date):
    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "outbound_date": departure_date,
        "return_date": return_date,
        "api_key": api_key,
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(response.text)

    response.raise_for_status()

    return response.json()