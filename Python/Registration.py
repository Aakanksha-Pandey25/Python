from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
# driver.get('')

driver.get("https://rahulshettyacademy.com/client")

driver.maximize_window()
register1=driver.find_element("xpath", "//a[text()='Register']")
register1.click()
time.sleep(20)
Fname = driver.find_element(By.ID, "firstName")
lname = driver.find_element(By.ID, "lastName")
email= driver.find_element(By.ID, "userEmail")
mobile = driver.find_element(By.ID, "userMobile")
occupation= driver.find_element(By.ID, "occupation")
password = driver.find_element(By.ID, "userPassword")
cpassword = driver.find_element(By.ID, "confirmPassword")
register = driver.find_element(By.ID, "Register")

Fname.send_keys("Aakaknsha")
lname.send_keys("pandey")
email.send_keys("akankshapandey@gmail.com")
mobile.send_keys("7489579384")
password.send_keys("admin")
cpassword.send_keys("admin")
register.click()

input("Press Enter to close the browser...")  # Keeps browser open until you press Enter
driver.quit()
