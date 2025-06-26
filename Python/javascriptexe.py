
'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://example.com")
driver.maximize_window()
element=driver.find_element(By.ID,"myButton")
driver.execute_script("argument[0].click();",element)
time.sleep(10)
driver.quit()'''
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(30)

mail=driver.find_element(By.ID,"userEmail")
driver.execute_script("argument[0].value='aakanksha';",mail)

password=driver.find_element(By.ID,"userPassword")
driver.execute_script("argument[0].value='aakanksha123';",password)

button=driver.find_element(By.ID,"login")
driver.execute_script("argument[0].click();",button)
time.sleep(5)
driver.quit()"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Launch the browser
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

# 2. Wait for manual CAPTCHA input or loading
time.sleep(30)

# 3. Set script timeout (important for async scripts)
driver.set_script_timeout(10)

# 4. Fill email using async JavaScript
mail = driver.find_element(By.ID, "userEmail")
driver.execute_async_script("""
    var element = arguments[0];
    var callback = arguments[arguments.length - 1];
    setTimeout(function() {
        element.value = 'aakanksha';
        callback();
    }, 500);  // simulate async with 0.5 sec delay
""", mail)

# 5. Fill password using async JavaScript
password = driver.find_element(By.ID, "userPassword")
driver.execute_async_script("""
    var element = arguments[0];
    var callback = arguments[arguments.length - 1];
    setTimeout(function() {
        element.value = 'aakanksha123';
        callback();
    }, 500);
""", password)

# 6. Click login button using async JavaScript
button = driver.find_element(By.ID, "login")
driver.execute_async_script("""
    var element = arguments[0];
    var callback = arguments[arguments.length - 1];
    setTimeout(function() {
        element.click();
        callback();
    }, 500);
""", button)

# 7. Wait to observe the result
time.sleep(5)

# 8. Close the browser
driver.quit()
