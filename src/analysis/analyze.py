import matplotlib.pyplot as plt
import pandas as pd
import os


def load_data(file_path):
    # Чтение данных из CSV файла
    df = pd.read_csv(file_path)

    # Извлекаем месяц, дату начала и дату окончания из столбца Weekend
    df['Month'] = df['Weekend'].str.split(' ').apply(lambda x: x[0])
    df['Start Day'] = df['Weekend'].str.split(' ').apply(lambda x: x[1].split('-')[0])
    df['End Day'] = df['Weekend'].str.split(' ').apply(lambda x: x[1].split('-')[1])

    # Преобразуем извлеченные данные в нужные форматы
    df['Start Day'] = pd.to_numeric(df['Start Day'], errors='coerce')
    df['End Day'] = pd.to_numeric(df['End Day'], errors='coerce')

    # Преобразование строк с денежными значениями в числа
    df['Weekend Gross'] = df['Weekend Gross'].replace('-', '0')
    df['Weekend Gross'] = df['Weekend Gross'].replace('[\$,]', '', regex=True).astype(float)

    return df

# Основной анализ
def analyze_data(df):
    # Группировка по регионам и вычисление суммарных сборов
    region_gross = df.groupby("Area")["Weekend Gross"].sum().sort_values(ascending=False).head(20)

    # Группировка по фильмам и вычисление суммарных сборов
    film_gross = df.groupby('#1 Release')['Weekend Gross'].sum().sort_values(ascending=False)

    # Динамика сборов по неделям
    weekly_gross = df.groupby([df['Month'], df['Start Day']])['Weekend Gross'].sum().sort_values(
        ascending=False).sort_index()


    # Топ фильмов по количеству недель на первом месте
    top_releases = df['#1 Release'].value_counts()

    return region_gross, film_gross, weekly_gross, top_releases

# Функция для визуализации и сохранения результатов
def save_results(data_dir, region_gross, film_gross, weekly_gross, top_releases):
    region_gross.to_excel(os.path.join(data_dir, "region_gross.xlsx"))
    film_gross.to_excel(os.path.join(data_dir, "film_gross.xlsx"))
    weekly_gross.to_excel(os.path.join(data_dir, "weekly_gross.xlsx"))
    top_releases.to_excel(os.path.join(data_dir, "top_releases.xlsx"))

    # Гистограмма сборов по регионам
    plt.figure(figsize=(10, 6))
    region_gross.plot(kind='bar', color='skyblue')
    plt.title('Суммарные сборы по ТОП-20 регионам')
    plt.xlabel('Регион')
    plt.ylabel('Сборы')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, "region_gross_hist.png"))


    # Гистограмма сборов по фильмам
    plt.figure(figsize=(10, 6))
    film_gross.head(10).plot(kind='bar', color='salmon')  # Топ-10 фильмов
    plt.title('Топ-10 фильмов по сборам')
    plt.xlabel('Фильм')
    plt.ylabel('Сборы')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, "film_gross_hist.png"))

    # Линейный график динамики сборов по неделям
    plt.figure(figsize=(10, 6))
    weekly_gross.plot(kind='line', color='green', marker='o', linestyle='-')
    plt.title('Динамика сборов по неделям')
    plt.xlabel('Неделя')
    plt.ylabel('Сборы')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, "weekly_gross_dynamic.png"))

    # Круговая диаграмма распределения сборов по регионам (Топ-5 регионов)
    plt.figure(figsize=(8, 8))
    region_gross.head(5).plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='coolwarm')
    plt.title('Распределение сборов по регионам (Топ-5)')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, "region_gross_piechart.png"))

    # Топ-5 фильмов по количеству недель на первом месте
    plt.figure(figsize=(10, 6))
    top_releases.head(5).plot(kind='bar', color='orange')
    plt.title('Топ-5 фильмов по количеству недель на первом месте')
    plt.xlabel('Фильм')
    plt.ylabel('Количество недель')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(data_dir, "top_releases_hist.png"))
