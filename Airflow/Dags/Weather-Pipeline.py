from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "you",
}

with DAG(
    dag_id="weather_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    default_args=default_args,
) as dag:

    fetch = BashOperator(
        task_id="fetch_weather",
        bash_command="python /opt/airflow/scripts/fetch_weather.py"
    )

    transform = BashOperator(
        task_id="transform_weather",
        bash_command="python /opt/airflow/scripts/transform_weather.py"
    )

    load = BashOperator(
        task_id="load_to_db",
        bash_command="python /opt/airflow/scripts/load_to_db.py"
    )

    fetch >> transform >> load

# Weather Data Pipeline DAG
#
# This Apache Airflow DAG runs an hourly ETL pipeline that:
# 1. Fetches weather data from an external source
# 2. Transforms and cleans the data
# 3. Loads the processed data into a database
#
# Task execution order:
# fetch_weather -> transform_weather -> load_to_db
#
# The DAG is scheduled to run every hour starting from
# January 1, 2024, with catchup disabled.
