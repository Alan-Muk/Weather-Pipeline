import json
import pandas as pd
import glob

def process_file(file):
    with open(file) as f:
        data = json.load(f)
    
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": data["dt"]
    }

def main():
    files = glob.glob("data/*.json")
    
    records = [process_file(f) for f in files]
    
    df = pd.DataFrame(records)
    df.to_csv("data/processed_weather.csv", index=False)
    
    print("Processed data saved!")

if __name__ == "__main__":
    main()