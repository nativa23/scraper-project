import schedule
import time
from src.scraper.parser import parse_boxoffice_mojo
from src.scraper.storage import save_to_csv
import os

def job():
    print("Запуск сбора данных...")
    movies = parse_boxoffice_mojo()
    if movies:
        # Указываем путь для сохранения файла в папку data
        data_folder = "../../data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)  # Создаём папку, если её нет
        save_to_csv(movies, os.path.join(data_folder, "movies.csv"))
        print("Сбор данных завершён, данные сохранены.")
    else:
        print("Нет данных для сохранения.")

# Планируем запуск каждый день в 9:00 утра
schedule.every().day.at("09:00").do(job)

print("Планировщик запущен. Ожидание следующего запуска...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверяем каждую минуту
