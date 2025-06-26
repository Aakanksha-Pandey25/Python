
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,"//a[contains(text(),'Alert with OK')]").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()
alert=driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(10)
driver.quit()

# //*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div/input
#root > div > div.MuiGrid-root.MuiGrid-container > div.MuiGrid-root.jss1206.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-12.MuiGrid-grid-md-8.MuiGrid-grid-xl-8 > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-3 > div:nth-child(1) > div > div > div > input