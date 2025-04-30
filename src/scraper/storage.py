import csv
import os

def save_to_csv(data, filepath):
    if not data:
        print("Нет данных для сохранения.")
        return

    keys = data[0].keys()  # Берём заголовки из первого элемента списка

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные сохранены в {filepath}")
