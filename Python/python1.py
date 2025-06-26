
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver=webdriver.Chrome
driver.get("https://rahulshettyacademy.com/client")

time.sleep(2)

email=driver.find_element(BY.ID,"username")
password =driver.find_element(BY.ID,"userpassword")
login =driver.find_element(BY.ID,"login")

email.send_keys("yffkf")
password.send_keys("fefges")
login.click()

input("Press Enter to close the browser...")  # Keeps browser open until you press Enter
driver.quit()
