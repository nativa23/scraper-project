from scraper import get_vacancies
from storage import save_to_csv

if __name__ == "__main__":
    try:
        vacancies = get_vacancies()
        if vacancies:
            print(f"Найдено {len(vacancies)} вакансий.")  # Выводим количество собранных вакансий
            save_to_csv(vacancies, "vacancies.csv")
            print("Сбор данных завершён.")
        else:
            print("Нет данных для сохранения.")
    except Exception as e:
        print(f"Ошибка при выполнении: {e}")


