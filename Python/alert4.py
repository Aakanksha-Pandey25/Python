
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
driver.find_element(By.XPATH,"//button[@class,'btn btn-primary']").click()
alert=driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(40)
driver.quit()
