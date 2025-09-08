from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

from main import open_page, go_to_registration, fill_registration_form, submit_registration, check_registration, generate_username


# --- Настройка браузера для GitHub Actions ---
def get_browser():
    """
    Создаёт экземпляр браузера Chrome в headless-режиме,
    чтобы он работал на GitHub Actions (без графического интерфейса).
    """
    options = Options()
    options.add_argument("--headless")  # без графического интерфейса
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


if __name__ == "__main__":
    browser = get_browser()

    try:
        # Шаг 1: открыть главную страницу
        open_page(browser, "https://parabank.parasoft.com/")

        # Шаг 2: перейти в раздел регистрации
        go_to_registration(browser)

        # Шаг 3: данные пользователя
        user_data = {
            "first_name": "Димка",
            "last_name": "Картинка",
            "address": "Улица Пушкина, дом Колотушкина",
            "city": "Москва",
            "state": "Московская область",
            "zip": "0000",
            "phone": "+123",
            "ssn": "0000",
            "username": generate_username(),
            "password": "pepe",
        }

        # Шаг 4: заполнить форму
        fill_registration_form(browser, user_data)

        # Шаг 5: отправить форму
        submit_registration(browser)

        # Шаг 6: проверить успешность регистрации
        check_registration(browser)

        # В GitHub Actions окно не видно, но можно подождать
        time.sleep(5)

    finally:
        browser.quit()

