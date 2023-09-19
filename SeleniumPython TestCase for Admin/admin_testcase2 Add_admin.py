from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the localhost URL
driver.get("http://localhost/gshop/admin/admin_login.php")
driver.maximize_window()

# Click the submit button

name_field = driver.find_element(By.CLASS_NAME, "name")
name_field.click()
name_field.send_keys("admin")

# Fill in the password

email_field = driver.find_element(By.CLASS_NAME, "pass")
email_field.click()
email_field.send_keys("111")

# Click the user button again

driver.find_element(By.CLASS_NAME, "sub").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, "adm").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "add_adm").click()

name_field11 = driver.find_element(By.CLASS_NAME, "admname")
name_field11.click()
name_field11.send_keys("Hriodoy")
time.sleep(3)

number_field2 = driver.find_element(By.CLASS_NAME, "admpass")
number_field2.click()
number_field2.send_keys("333")

number_field3 = driver.find_element(By.CLASS_NAME, "readmpass")
number_field3.click()
number_field3.send_keys("333")

time.sleep(3)
driver.find_element(By.CLASS_NAME, "sub2").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "adm").click()
time.sleep(3)
