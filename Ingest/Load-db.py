import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="weather",
    user="admin",
    password="admin",
    port=5432
)

cur = conn.cursor()

df = pd.read_csv("Data/processed_weather.csv")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO weather_data (city, temperature, humidity, wind_speed, timestamp)
        VALUES (%s, %s, %s, %s, to_timestamp(%s))
    """, (
        row["city"],
        row["temperature"],
        row["humidity"],
        row["wind_speed"],
        row["timestamp"]
    ))

conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL!")

# Weather Data Loading Script
#
# This script loads processed weather data from a CSV file
# into a PostgreSQL database.
#
# Main steps:
# 1. Connect to the PostgreSQL weather database
# 2. Read processed weather data from a CSV file
# 3. Insert each weather record into the weather_data table
# 4. Commit the transaction and close the database connection
#
# The script uses pandas for CSV processing and psycopg2
# for PostgreSQL database operations.
#
# Source file:
# Data/processed_weather.csv
#
# Target table:
# weather_data
#
# Inserted fields:
# city, temperature, humidity, wind_speed, timestamp
