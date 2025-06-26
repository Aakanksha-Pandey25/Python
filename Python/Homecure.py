
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://homecureph1drindranil-203321-react.b203321.dev.eastus.az.svc.builder.cafe")

number=7489579384

driver.find_element(By.XPATH, "//span[text()='Patient']").click()
#Hospital=driver.find_element(By.XPATH,"//span[text()='Hospital']").click()
#HealthcarePersonal=driver.find_element(By.XPATH,"//span[@class='MuiButton-label']").click()
driver.find_element(By.XPATH,"//span[text()='CONTINUE']").click()


driver.find_element(By.XPATH,"//input[@type='text']").send_keys(number)
driver.find_element(By.XPATH,"//span[text()='Log in']").click()

driver.find_element(By.ID,"otpInput0").send_keys(1)
driver.find_element(By.ID,"otpInput1").send_keys(2)
driver.find_element(By.ID,"otpInput2").send_keys(3)
driver.find_element(By.ID,"otpInput3").send_keys(4)
driver.find_element(By.XPATH,"//span[text()='Verify']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Done']").click()

driver.find_element(By.XPATH,"//input[@placedholder='Enter your mail id ']").send_keys("pandey@gmail.com")
driver.find_element(By.XPATH,"//span[text()='Continue']").click()

driver.find_element(By.XPATH,"//input[@placeholder='Enter your name']").send_keys("Aakanksha")
print("filled the name")
driver.find_element(By.XPATH,"//input[@placeholder='Enter your address']").send_keys("malwa mill")
driver.find_element(By.XPATH,"//input[@placeholder='Enter city']").send_keys("Indore")
driver.find_element(By.XPATH,"//input[@placeholder='Enter district']").send_keys("Indore")
driver.find_element(By.XPATH,"//input[@placeholder='6 digit Pin Code']").send_keys("452008")
driver.find_element(By.XPATH,"//input[@placeholder='Enter age']").send_keys("22")
driver.find_element(By.XPATH,"//input[@placeholder='Enter family member name']").send_keys("Rashi")
driver.find_element(By.XPATH,"//input[@placeholder='Enter family member relation']").send_keys("Sister")
driver.find_element(By.XPATH,"//input[@placeholder='Enter phone number']").send_keys("9977907050")
driver.find_element(By.XPATH,"//span[text()='Submit']").click()

time.sleep(20)

