
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"tabButton").click()
tabs=driver.window_handles
driver.switch_to.window(tabs[1])
print("new tab title", driver.title)
time.sleep(10)

body_text = driver.find_element(By.TAG_NAME, "body").text
print("Text from new tab:", body_text)

# Switch back to the original tab
driver.switch_to.window(tabs[0])
print("Back to original tab:", driver.title)

driver.quit()

