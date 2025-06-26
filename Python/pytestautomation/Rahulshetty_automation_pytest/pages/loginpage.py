from selenium.webdriver.common.by import By
from pytestautomation.Rahulshetty_automation_pytest.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "userEmail")
    PASSWORD_INPUT = (By.ID, "userPassword")
    LOGIN_BTN = (By.ID, "login")

    def go_to_login(self):
        self.driver.get("https://rahulshettyacademy.com/client")

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
