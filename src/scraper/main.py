from src.scraper.parser import parse_boxoffice_mojo
from src.scraper.storage import save_to_csv
import os


if __name__ == "__main__":
    movies = parse_boxoffice_mojo()
    if movies:
        data_folder = os.path.join("..", "..", "data")
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)  # Создаём папку, если её нет
        save_to_csv(movies, os.path.join(data_folder, "movies.csv"))
        print("Сбор данных завершён, сохранено в movies.csv")
    else:
        print("Нет данных для сохранения.")
