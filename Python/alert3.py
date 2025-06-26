
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'Alert with Textbox ')]").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
alert=driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(20)
driver.quit()