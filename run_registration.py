from selenium import webdriver
from main import open_page, go_to_registration, fill_registration_form, submit_registration, check_registration, \
    generate_username
import time

browser = webdriver.Chrome()
browser.maximize_window()

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

    # Шаг 7: подождать 30 секунд, чтобы увидеть результат
    time.sleep(30)

finally:
    browser.quit()
