import time
import random
import string
from selenium.webdriver.common.by import By

def open_page(browser, url):
    browser.get(url)
    time.sleep(3)

def go_to_registration(browser):
    browser.find_element(By.CSS_SELECTOR, "a[href='register.htm']").click()
    time.sleep(2)

def fill_field(browser, selector, value):
    field = browser.find_element(By.CSS_SELECTOR, selector)
    field.send_keys(value)

def fill_registration_form(browser, data):
    fill_field(browser, "input[id='customer.firstName']", data["first_name"])
    fill_field(browser, "input[id='customer.lastName']", data["last_name"])
    fill_field(browser, "input[id='customer.address.street']", data["address"])
    fill_field(browser, "input[id='customer.address.city']", data["city"])
    fill_field(browser, "input[id='customer.address.state']", data["state"])
    fill_field(browser, "input[id='customer.address.zipCode']", data["zip"])
    fill_field(browser, "input[id='customer.phoneNumber']", data["phone"])
    fill_field(browser, "input[id='customer.ssn']", data["ssn"])
    fill_field(browser, "input[id='customer.username']", data["username"])
    fill_field(browser, "input[id='customer.password']", data["password"])
    fill_field(browser, "input[id='repeatedPassword']", data["password"])

def submit_registration(browser):
    browser.find_element(By.CSS_SELECTOR, '[value="Register"]').click()
    time.sleep(3)

def check_registration(browser):
    if browser.current_url == "https://parabank.parasoft.com/parabank/register.htm":
        print("Регистрация успешна")
    else:
        print("Регистрация не удалась, текущий URL:", browser.current_url)

def generate_username(base="dimka"):
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{base}_{suffix}"
