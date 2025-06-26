
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/client")


register1=driver.find_element("xpath", "//a[text()='Register']")
register1.click()

Email="Aakankshapandey2@gmail.com"
Password="Aakanksha@123"
fname=driver.find_element(By.ID,"firstName")
lname=driver.find_element(By.ID,"lastName")
email=driver.find_element(By.ID,"userEmail")
mobile=driver.find_element(By.ID,"userMobile")
gender=driver.find_element(By.XPATH,"//input[@type='radio' and @value='Female']")
password=driver.find_element(By.ID,"userPassword")
confirmpass=driver.find_element(By.ID,"confirmPassword")
checkb=driver.find_element(By.XPATH,"//input[@type='checkbox']")
dropdownE = driver.find_element(By.XPATH, "//select[contains(@class, 'custom-select')]")
dropdown=Select(dropdownE)  # object of dropdown
dropdown.select_by_visible_text("Engineer")
register=driver.find_element(By.ID,"login")

fname.send_keys("Aakaknsha")
lname.send_keys("padey")
email.send_keys(Email)
mobile.send_keys("1234567890")
password.send_keys(Password)
confirmpass.send_keys(Password)
gender.click()
checkb.click()
register.click()
#register=driver.find_element(By.ID,"login")
login=driver.find_element(By.XPATH,"//button[text()='Login']")
login.click()

email=driver.find_element(By.ID,"userEmail")
password=driver.find_element(By.ID,"userPassword")
Login=driver.find_element(By.ID,"login")
email.send_keys(Email)
password.send_keys(Password)
Login.click()


time.sleep(20)
