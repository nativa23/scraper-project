from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Параметры DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 3, 23),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# Функция для запуска main.py
def run_scraper():
    subprocess.run(["python", "/path/to/main.py"], check=True)

# Определяем DAG
dag = DAG(
    "hh_scraper",
    default_args=default_args,
    description="Парсер вакансий системных аналитиков с hh.ru",
    schedule_interval="0 9 * * *",  # Запуск каждый день в 9:00
    catchup=False,
)

# Создаём задачу
scraper_task = PythonOperator(
    task_id="run_scraper",
    python_callable=run_scraper,
    dag=dag,
)

scraper_task
