from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
# driver.get('')

driver.get("https://rahulshettyacademy.com/client")
time.sleep(2)

email = driver.find_element(By.ID, "userEmail")
password = driver.find_element(By.ID, "userPassword")
login = driver.find_element(By.ID, "login")

email.send_keys("yffkf")
password.send_keys("fefges")
login.click()

input("Press Enter to close the browser...")  # Keeps browser open until you press Enter
driver.quit()
