import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from main import open_page, go_to_registration, fill_registration_form, submit_registration, generate_username

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

# --- Функция логина ---
def login(browser, username, password):
    """
    Вводит логин и пароль на главной странице и нажимает кнопку Log In
    """
    browser.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
    browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
    time.sleep(2)

# --- Проверка успешного логина ---
def check_login(browser):
    """
    Проверяет, что после авторизации мы попали на страницу overview (личный кабинет).
    """
    assert browser.current_url.endswith("/parabank/overview.htm"), \
        f"Логин не удался, текущий URL: {browser.current_url}"

# --- Сам тест ---
def test_login():
    """
    Полный тест:
    1. Регистрируем нового пользователя
    2. Выполняем логин с зарегистрированными данными
    3. Проверяем, что вход выполнен успешно
    """
    browser = get_browser()

    try:
        # Шаг 1: открываем главную страницу сайта
        open_page(browser, "https://parabank.parasoft.com/")

        # Шаг 2: переходим в форму регистрации
        go_to_registration(browser)

        # Шаг 3: формируем тестовые данные для пользователя
        user_data = {
            "first_name": "Димка",
            "last_name": "Картинка",
            "address": "Улица Пушкина, дом Колотушкина",
            "city": "Москва",
            "state": "Московская область",
            "zip": "0000",
            "phone": "+123",
            "ssn": "0000",
            "username": generate_username(),  # уникальный username при каждом запуске
            "password": "pepe",
        }

        # Шаг 4: заполняем форму регистрации
        fill_registration_form(browser, user_data)

        # Шаг 5: отправляем форму регистрации
        submit_registration(browser)

        # Шаг 6: возвращаемся на главную страницу (для авторизации)
        open_page(browser, "https://parabank.parasoft.com/parabank/index.htm")

        # Шаг 7: выполняем логин под только что зарегистрированным пользователем
        login(browser, user_data["username"], user_data["password"])

        # Шаг 8: проверяем, что логин успешен
        check_login(browser)

    finally:
        browser.quit()
