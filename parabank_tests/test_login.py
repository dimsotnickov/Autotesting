from selenium import webdriver
from main import open_page, go_to_registration, fill_registration_form, submit_registration, generate_username
import time
from selenium.webdriver.common.by import By

def login(browser, username, password):
    """Вводим данные логина и нажимаем Log In"""
    browser.find_element("css selector", "input[name='username']").send_keys(username)
    browser.find_element("css selector", "input[name='password']").send_keys(password)
    browser.find_element("css selector", "input[value='Log In']").click()
    time.sleep(3)

def check_login(browser):
    """Проверяем, что логин успешен"""
    if browser.current_url.endswith("/parabank/overview.htm"):
        print("Логин успешен")
    else:
        print("Логин не удался, текущий URL:", browser.current_url)

browser = webdriver.Chrome(options=options)
browser.maximize_window()

try:
    # Регистрация
    open_page(browser, "https://parabank.parasoft.com/")
    go_to_registration(browser)

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

    fill_registration_form(browser, user_data)
    submit_registration(browser)

    print("Регистрация завершена. Переходим к логину...")


    ### Т.к. мы после регистрации попадаем сразу в ЛК, чтобы проверить успешно регистрации - сначала разлогинимся
    log_out = browser.find_element(By.CSS_SELECTOR, "a[href='logout.htm']").click()
    time.sleep(5)

    # Логин после регистрации и разлогина
    login(browser, user_data["username"], user_data["password"])
    time.sleep(3)
    check_login(browser)

    # Ждём 30 секунд, чтобы увидеть результат
    time.sleep(30)

finally:
    browser.quit()

