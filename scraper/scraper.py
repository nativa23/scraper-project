from parser import parse_vacancies

def get_vacancies():
    """
    Запускает процесс парсинга и возвращает список вакансий.
    """
    vacancies = parse_vacancies()
    return vacancies
