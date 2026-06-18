import requests
import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load env variables
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("API KEY LOADED:", API_KEY)

CITIES = ["Amsterdam", "London", "New York"]


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"\n❌ Error for {city}")
        print("Status:", response.status_code)
        print("Response:", response.text)
        return None

    return response.json()


def save_raw_data(city, data):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

    data_dir = BASE_DIR / "data"
    data_dir.mkdir(exist_ok=True)

    filename = data_dir / f"{city}_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    print(f"Saved data for {city}")


def main():
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            save_raw_data(city, data)


if __name__ == "__main__":
    main()

# Weather Data Fetching Script
#
# This script retrieves current weather data for a list of cities
# using the OpenWeather API.
#
# Main steps:
# 1. Load API credentials from a .env configuration file
# 2. Send API requests for each city
# 3. Validate API responses and handle errors
# 4. Save raw weather data as timestamped JSON files
#
# The script currently fetches weather data for:
# Amsterdam, London, and New York.
#
# Output files are stored in the Data/ directory and include
# timestamps to preserve historical records.
