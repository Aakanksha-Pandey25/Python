
'''from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")
expected_tilte="Let's Shop"
actual_title= "driver.title()"

assert actual_title == expected_tilte , "Title matched successfully"
assert True
driver.quit()'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

expected_title = "Let's Shop"
driver.get("https://rahulshettyacademy.com")

actual_title = driver.title

if actual_title == expected_title:
 assert True
 print("successfully")

driver.close()