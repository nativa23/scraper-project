from typing import TextIO
import csv

def save_to_csv(vacancies: list[dict[str, str]], filename: str) -> None:
    """
    Сохраняет список вакансий в CSV-файл.
    """
    if not vacancies:
        print("Нет данных для сохранения.")
        return

    with open(filename, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["title", "company", "salary"])  # PyCharm больше не ругается
        writer.writeheader()
        writer.writerows(vacancies)

    print(f"Данные сохранены в {filename}")
