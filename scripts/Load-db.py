import pandas as pd
import sqlite3

# Load processed data
df = pd.read_csv("data/processed_weather.csv")

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("weather.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    humidity INTEGER,
    wind_speed REAL,
    timestamp INTEGER
)
""")

# Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO weather_data (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        row["city"],
        row["temperature"],
        row["humidity"],
        row["wind_speed"],
        row["timestamp"]
    ))

conn.commit()
conn.close()

print("Data loaded into SQLite (weather.db)!")