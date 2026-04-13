 Weather Data Engineering Pipeline


---

 Project Overview

This project demonstrates how to build a production-style data pipeline that:

* Extracts weather data from an external API
* Stores raw data for traceability
* Transforms data into analytics-ready format
* Loads data into a PostgreSQL database
* Automates workflows using Apache Airflow

---

 Architecture

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

 Tech Stack

* **Python** – Data ingestion & transformation
* **PostgreSQL** – Data storage
* **Apache Airflow** – Workflow orchestration
* **Docker / Podman** – Containerized environment
* **Pandas** – Data processing
* **Requests** – API calls

---

 Project Structure

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

 Features

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

---

 Install dependencies

```bash
pip install -r requirements.txt
```

---

 Run PostgreSQL (Podman)

```bash
podman run -d \
  --name weather-db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=weather \
  -p 5432:5432 \
  docker.io/library/postgres:15
```

---
 Run the pipeline manually

```bash
python ingestion/fetch_weather.py
python ingestion/transform_weather.py
python ingestion/load_to_db.py
```

---

### 6. Start Airflow

```bash
podman-compose up -d
```

Access Airflow UI:
http://localhost:8080

---
 Example Use Cases

* Track temperature trends across cities
* Analyze humidity and wind patterns
* Build dashboards for weather analytics
* Extend to climate monitoring systems

---
 Future Improvements

* Add Streamlit dashboard for visualization
* Implement dbt for advanced transformations
* Add data quality checks and validation
* Deploy pipeline to cloud (AWS/GCP/Azure)
* Implement real-time streaming pipeline

---

 Key Learnings

* Building end-to-end data pipelines
* Working with REST APIs
* Data modeling and transformation
* Workflow orchestration with Airflow
* Containerized development environments

---



