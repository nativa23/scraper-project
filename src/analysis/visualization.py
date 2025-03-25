import matplotlib.pyplot as plt
import pandas as pd

# Функция для визуализации
def visualize_data(region_gross, film_gross, weekly_gross, top_releases):
    # Гистограмма сборов по регионам
    plt.figure(figsize=(10, 6))
    region_gross.plot(kind='bar', color='skyblue')
    plt.title('Суммарные сборы по регионам')
    plt.xlabel('Регион')
    plt.ylabel('Сборы')
    plt.show()

    # Гистограмма сборов по фильмам
    plt.figure(figsize=(10, 6))
    film_gross.plot(kind='bar', color='salmon')
    plt.title('Суммарные сборы по фильмам')
    plt.xlabel('Фильм')
    plt.ylabel('Сборы')
    plt.show()

    # Линейный график динамики сборов по неделям
    plt.figure(figsize=(10, 6))
    weekly_gross.plot(kind='line', color='green', marker='o')
    plt.title('Динамика сборов по неделям')
    plt.xlabel('Неделя')
    plt.ylabel('Сборы')
    plt.show()

    # Круговая диаграмма распределения сборов по регионам
    plt.figure(figsize=(10, 6))
    region_gross.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Распределение сборов по регионам')
    plt.ylabel('')
    plt.show()

    # Топ 5 фильмов по числу релизов
    plt.figure(figsize=(10, 6))
    top_releases.head(5).plot(kind='bar', color='orange')
    plt.title('Топ 5 фильмов по количеству релизов')
    plt.xlabel('Фильм')
    plt.ylabel('Количество релизов')
    plt.show()

# Пример вызова:
# visualize_data(region_gross, film_gross, weekly_gross, top_releases)
