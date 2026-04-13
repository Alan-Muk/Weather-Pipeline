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