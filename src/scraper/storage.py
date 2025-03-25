import csv
import os

def save_to_csv(data, filename):
    if not data:
        print("Нет данных для сохранения.")
        return

    # Создаём папку data, если её нет
    os.makedirs("data", exist_ok=True)

    filepath = os.path.join("data", filename)

    keys = data[0].keys()  # Берём заголовки из первого элемента списка

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные сохранены в {filepath}")
