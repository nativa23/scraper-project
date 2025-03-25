from src.scraper.parser import parse_boxoffice_mojo
from src.scraper.storage import save_to_csv

if __name__ == "__main__":
    movies = parse_boxoffice_mojo()
    if movies:
        save_to_csv(movies, "movies.csv")
        print("Сбор данных завершён, сохранено в movies.csv")
    else:
        print("Нет данных для сохранения.")
