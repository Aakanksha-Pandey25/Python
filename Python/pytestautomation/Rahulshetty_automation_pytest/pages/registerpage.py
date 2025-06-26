from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    NAME = (By.ID,"firstName")
    LANAME=(By.ID,"lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE=(By.ID,"userMobile")
    GENDER=(By.XPATH,"//input[@type='radio' and @value='Female']")
    USER_TYPE = (By.XPATH, "//input[@value='Student']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Passsword']")
    CONFIRM = (By.XPATH, "//input[@name='confirmPassword']")
    REGISTER_BTN = (By.XPATH, "//input[@placeholder='Confirm Passsword']")

    def go_to_register(self):
        self.driver.get("https://rahulshettyacademy.com/client/auth/register")

    def register_user(self, name,lname, email,mobile, password):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.LANAME).send_keys(lname)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.MOBILE).send_keys(mobile)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM).send_keys(password)
        self.driver.find_element(*self.GENDER).click()
        self.driver.find_element(*self.USER_TYPE).click()
        self.driver.find_element(*self.REGISTER_BTN).click()
