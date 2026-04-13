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