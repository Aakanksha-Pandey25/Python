
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,"//a[contains(text(),'Alert with OK & Cancel ')]").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
alert=driver.switch_to.alert
print("Alert text:", alert.text)
alert.dismiss()
time.sleep(10)
driver.quit()

