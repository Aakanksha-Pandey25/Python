import time
import random
import string
from pages.registerpage import RegisterPage
from pages.loginpage import LoginPage

def generate_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@test.com"

def test_register_and_login(driver):
    email = generate_email()
    password = "Test@123"
    name = "Test User"
    lname="pandey"
    mobile="9977907050"

    register = RegisterPage(driver)
    register.go_to_register()
    register.register_user(name,lname,email,mobile,password)

    time.sleep(2)  # wait for registration to complete

    login = LoginPage(driver)
    login.go_to_login()
    login.login(email, password)

    time.sleep(2)
    assert "dashboard" in driver.current_url
