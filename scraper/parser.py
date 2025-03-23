from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def parse_vacancies():
    # Настройка Selenium
    options = Options()
    options.add_argument("--headless")  # Убирай, если хочешь увидеть браузер
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&context=H4sIAAAAAAAA_wEjANz_YToxOntzOjg6ImZyb21QYWdlIjtzOjc6ImNhdGFsb2ciO312FITcIwAAAA"
    print("Открываем сайт...")
    driver.get(url)

    # Ожидаем загрузки страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "catalog-serp")))
    print("Страница загружена. Начинаем парсинг...")

    vacancies = []
    job_elements = driver.find_elements(By.CLASS_NAME, "product-card__wrapper")
    print(f"Найдено {len(job_elements)} вакансий.")

    for item in job_elements:
        try:
            title = item.find_element(By.CLASS_NAME, "iva-item-title-CdRXl").text.strip()
        except:
            title = "Не указано"

        try:
            company = item.find_element(By.CLASS_NAME, "vacancy-serp__vacancy-employer-text").text.strip()
        except:
            company = "Не указано"

        try:
            salary_element = item.find_element(By.CLASS_NAME, "bloko-header-section-3")
            salary = salary_element.text.strip() if salary_element else "Не указана"
        except:
            salary = "Не указана"

        vacancies.append({"title": title, "company": company, "salary": salary})

        # Выводим каждую вакансию, которую собираем
        print(f"Вакансия: {title}, Компания: {company}, Зарплата: {salary}")

    driver.quit()
    return vacancies

