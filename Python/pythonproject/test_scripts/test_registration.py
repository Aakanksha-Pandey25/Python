import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("DEBUG sys.path:", sys.path)

import random, string
from selenium import webdriver
from pages.registration_page import RegistrationPage
import time

def generate_random_mobile():
    return str(random.randint(6000000000, 9999999999))

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["gmail.com", "yahoo.com", "test.com"])
    return f"{name}@{domain}"

def test_register_patient(browser):
    phone = generate_random_mobile()
    email = generate_random_email()

    try:
      page = RegistrationPage(browser)
      browser.get("https://homecureph1drindranil-203321-react.b203321.dev.eastus.az.svc.builder.cafe")
      page.register_user(phone, email)
      page.fill_personal_details()
    finally:
      time.sleep(5)  # Optional: for visual verification
      browser.quit()


if __name__ == "__main__":
    browser = webdriver.Chrome() 
    browser.maximize_window()
    test_register_patient(browser)