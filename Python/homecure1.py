
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

def generate_random_mobile():
    return str(random.randint(6000000000, 9999999999))  # Starts with 6-9

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["gmail.com", "yahoo.com", "test.com"])
    return f"{name}@{domain}"

random_mobile = generate_random_mobile() # assigning a variable
random_email = generate_random_email()

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://homecureph1drindranil-203321-react.b203321.dev.eastus.az.svc.builder.cafe")

driver.find_element(By.XPATH, "//span[text()='Patient']").click()
driver.find_element(By.XPATH,"//span[text()='CONTINUE']").click()

driver.find_element(By.XPATH,"//p[text()='Register']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//input[@placeholder='Enter your phone number']").send_keys(random_mobile)
driver.find_element(By.XPATH,"//span[text()='Continue']").click()
time.sleep(5)
driver.find_element(By.ID,"otpInput0").send_keys(1)
driver.find_element(By.ID,"otpInput1").send_keys(2)
driver.find_element(By.ID,"otpInput2").send_keys(3)
driver.find_element(By.ID,"otpInput3").send_keys(4)
driver.find_element(By.XPATH,"//span[text()='Verify']").click()
driver.find_element(By.XPATH,"//span[text()='Done']").click()
driver.find_element(By.XPATH,"//input[@placeholder = 'Enter your mail id ']").send_keys(random_email)
driver.find_element(By.XPATH,"//span[text()='Continue']").click()
driver.find_element(By.XPATH,"//span[text()='Resend']").click()
driver.find_element(By.XPATH,"//span[text()='Done']").click()

driver.find_element(By.XPATH,"//input[@placeholder='Enter your name']").send_keys("Tina")
driver.find_element(By.XPATH,"//input[@placeholder='Enter your address']").send_keys("malwa mill")
driver.find_element(By.XPATH,"//input[@placeholder='Enter city']").send_keys("Indore")
driver.find_element(By.XPATH,"//input[@placeholder='Enter district']").send_keys("Indore")
driver.find_element(By.XPATH,"//input[@placeholder='6 digit Pin Code']").send_keys("452008")
driver.find_element(By.XPATH,"//input[@placeholder='Enter age']").send_keys("22")
driver.find_element(By.XPATH,"//input[@placeholder='Enter family member name']").send_keys("Rashi")
driver.find_element(By.XPATH,"//input[@placeholder='Enter family member relation']").send_keys("Sister")
driver.find_element(By.XPATH,"//input[@placeholder='Enter phone number']").send_keys("9977907050")
driver.find_element(By.XPATH,"//div[contains(@class, 'css-1hwfws3']").click()
driver.find_element(By.XPATH,"//*[text()='Female']").click()
driver.find_element(By.XPATH, "//div[@data-test-id='paientLanguage']").click()
driver.find_element(By.XPATH, "//*[@id='language']/div/div[2]/div/div/div[2]").click()
driver.find_element(By.XPATH, "//*[@id='language']/div/div[2]/div/div/div[1]").click()
time.sleep(10)
#driver.find_element(By.XPATH,"//span[text()='Submit']").click()