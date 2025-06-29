
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get(" https://demoqa.com/buttons")
time.sleep(2)
driver.maximize_window()
action=ActionChains(driver)

double_click_button=driver.find_element(By.ID,"doubleClickBtn")
action.context_click(double_click_button).perform()
right_click_btn = driver.find_element(By.ID, "rightClickBtn")
action.context_click(right_click_btn).perform()


time.sleep(10)
print("completed")
