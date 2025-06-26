
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    PATIENT_TAB = (By.XPATH, "//span[text()='Patient']")
    CONTINUE_BTN = (By.XPATH, "//span[text()='CONTINUE']")
    REGISTER_LINK = (By.XPATH, "//p[text()='Register']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Enter your phone number']")
    CONTINUE_PHONE_BTN = (By.XPATH, "//span[text()='Continue']")
    OTP_FIELDS = [(By.ID, f"otpInput{i}") for i in range(4)]
    VERIFY_BTN = (By.XPATH, "//span[text()='Verify']")
    DONE_BTN = (By.XPATH, "//span[text()='Done']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter your mail id ']")
    CONTINUE_BTN1=(By.XPATH,"//span[text()='Continue']")
    RESEND_BTN = (By.XPATH, "//span[text()='Resend']")
    DONE_BTN1=(By.XPATH,"//span[text()='Done']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your name']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Enter your address']")
    CITY_INPUT = (By.XPATH, "//input[@placeholder='Enter city']")
    DISTRICT_INPUT = (By.XPATH, "//input[@placeholder='Enter district']")
    PINCODE_INPUT = (By.XPATH, "//input[@placeholder='6 digit Pin Code']")
    AGE_INPUT = (By.XPATH, "//input[@placeholder='Enter age']")
    FAMILY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Enter family member name']")
    FAMILY_RELATION_INPUT = (By.XPATH, "//input[@placeholder='Enter family member relation']")
    FAMILY_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Enter phone number']")
    GENDER_DROPDOWN = (By.XPATH, "//div[contains(@class, 'css-1hwfws3')]")
    GENDER_OPTION = (By.XPATH, "//*[text()='Female']")
    LANGUAGE_DROPDOWN = (By.XPATH, "//div[@data-test-id='paientLanguage']")
    LANGUAGE_ENGLISH = (By.XPATH, "//*[@id='language']/div/div[2]/div/div/div[2]")
    LANGUAGE_HINDI = (By.XPATH, "//*[@id='language']/div/div[2]/div/div/div[1]")
    SUBMIT_BTN = (By.XPATH, "//span[text()='Submit']")

    def register_user(self, phone, email):
        self.click(self.PATIENT_TAB)
        self.click(self.CONTINUE_BTN)
        self.click(self.REGISTER_LINK)
        self.enter_text(self.PHONE_INPUT, phone)
        self.click(self.CONTINUE_PHONE_BTN)

        for i, field in enumerate(self.OTP_FIELDS):
            self.enter_text(field, str(i+1))

        self.click(self.VERIFY_BTN)
        self.click(self.DONE_BTN)
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.CONTINUE_BTN1)
        self.click(self.RESEND_BTN)
        self.click(self.DONE_BTN)

    def fill_personal_details(self):
        self.enter_text(self.NAME_INPUT, "Tina")
        self.enter_text(self.ADDRESS_INPUT, "malwa mill")
        self.enter_text(self.CITY_INPUT, "Indore")
        self.enter_text(self.DISTRICT_INPUT, "Indore")
        self.enter_text(self.PINCODE_INPUT, "452008")
        self.enter_text(self.AGE_INPUT, "22")
        self.enter_text(self.FAMILY_NAME_INPUT, "Rashi")
        self.enter_text(self.FAMILY_RELATION_INPUT, "Sister")
        self.enter_text(self.FAMILY_PHONE_INPUT, "9977907050")
        self.click(self.GENDER_DROPDOWN)
        self.click(self.GENDER_OPTION)
        self.click(self.LANGUAGE_DROPDOWN)
        self.click(self.LANGUAGE_ENGLISH)
        self.click(self.LANGUAGE_HINDI)
        self.click(self.SUBMIT_BTN)
