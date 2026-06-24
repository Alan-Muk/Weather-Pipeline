# Weather Data Engineering Pipeline


---

# Project Overview

This project demonstrates how to build a production-style data pipeline that:

* Extracts weather data from an external API
* Stores raw data for traceability
* Transforms data into analytics-ready format
* Loads data into a PostgreSQL database
* Automates workflows using Apache Airflow

---

# Architecture

```
OpenWeatherMap API
        ↓
   Ingestion (Python)
        ↓
   Raw Storage (JSON files)
        ↓
   Transformation (Pandas)
        ↓
   PostgreSQL Database
        ↓
   Orchestration (Airflow)
```

---

# Tech Stack

* **Python** – Data ingestion & transformation
* **PostgreSQL** – Data storage
* **Apache Airflow** – Workflow orchestration
* **Docker / Podman** – Containerized environment
* **Pandas** – Data processing
* **Requests** – API calls

---

# Project Structure

```
weather-pipeline/
│
├── ingestion/
│   ├── fetch_weather.py
│   ├── transform_weather.py
│   └── load_to_db.py
│
├── airflow/
│   └── dags/
│       └── weather_pipeline.py
│
├── data/
│   ├── raw/
│   └── processed_weather.csv
│
├── config/
│   └── .env
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Features

* Multi-city weather data ingestion (e.g. Amsterdam, London, New York)
* Raw data storage for reproducibility
* Structured transformation pipeline
* Automated scheduling with Airflow
* Containerized setup for portability

---
 Setup Instructions

 Clone the repository

```bash
git clone https://github.com/your-username/weather-pipeline.git
cd weather-pipeline
```

---

 Create environment variables

Create a `.env` file in the `config/` folder:

```
OPENWEATHER_API_KEY=your_api_key_here
```

Get your API key from OpenWeatherMap.



