from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com")
driver.maximize_window()

time.sleep(2)
driver.save_screenshot("screenshot.png")
print("ss taken successfully")
driver.quit()