@echo off
cd  C:\Users\nivan\PycharmProjects\scraper-project
.venv\Scripts\activate.bat
python airflow/dags/flow.py
pause
