import pandas as pd


# Загрузка данных
def load_data(file_path):
    return pd.read_csv(file_path)


# Основной анализ
def analyze_data(df):
    # Группировка по регионам и вычисление суммарных сборов
    region_gross = df.groupby('Area')['Weekend Gross'].sum().sort_values(ascending=False)

    # Группировка по фильмам и вычисление суммарных сборов
    film_gross = df.groupby('#1 Release')['Weekend Gross'].sum().sort_values(ascending=False)

    # Пример анализа по регионам и неделям
    weekly_gross = df.groupby('Weekend')['Weekend Gross'].sum()

    # Пример: Найти фильмы, которые были в топе несколько раз
    top_releases = df.groupby('#1 Release').size().sort_values(ascending=False)

    # Вернуть данные для дальнейшей визуализации
    return region_gross, film_gross, weekly_gross, top_releases

# Пример вызова:
# df = load_data("movies.csv")
# region_gross, film_gross, weekly_gross, top_releases = analyze_data(df)
