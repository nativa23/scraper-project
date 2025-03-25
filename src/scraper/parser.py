from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def parse_boxoffice_mojo():
    options = Options()
    options.add_argument("--headless")  # Фоновый режим
    options.add_argument("--disable-blink-features=AutomationControlled")  # Обход защиты
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_rs_tab"
    driver.get(url)

    # Дожидаемся полной загрузки страницы
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # Найдём все строки таблицы
    rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'a-bordered')]/tbody/tr")

    data = []

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")

        if not cols:
            print("Пропущена пустая строка")
            continue

        # Проверим, есть ли хотя бы 6 столбцов
        if len(cols) < 6:
            print("Пропущена строка, так как в ней недостаточно столбцов:", [col.text for col in cols])
            continue

        try:
            area = cols[0].text.strip()  # Регион
            weekend = cols[1].text.strip()  # Дата уикенда
            releases = cols[2].text.strip()  # Количество релизов
            top_release = cols[3].text.strip()  # Лучший релиз
            distributor = cols[4].text.strip()  # Дистрибьютор
            weekend_gross = cols[5].text.strip()  # Кассовые сборы за уикенд

            data.append({
                "Area": area,
                "Weekend": weekend,
                "Releases": releases,
                "#1 Release": top_release,
                "Distributor": distributor,
                "Weekend Gross": weekend_gross
            })

        except Exception as e:
            print(f"Ошибка при обработке строки: {e}")

    driver.quit()
    return data


# Тестовый запуск
box_office_data = parse_boxoffice_mojo()

for entry in box_office_data:
    print(entry)
