from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the localhost URL
driver.get("http://localhost/gshop/contact.php")
driver.maximize_window()

# Click the user button
driver.find_element(By.ID, "contact").click()

# Fill in the email
time.sleep(3)
email_field = driver.find_element(By.CLASS_NAME, "user_name")
email_field.click()
email_field.send_keys("Sifat")
time.sleep(3)
user_number_field = driver.find_element(By.CLASS_NAME, "user_number")
user_number_field.click()
user_number_field.send_keys("01723903205")

email_field = driver.find_element(By.CLASS_NAME, "user_email")
email_field.click()
email_field.send_keys("sifat@gmail.com")

mess_button = driver.find_element(By.CLASS_NAME, "user_message")
mess_button.click()
mess_button.send_keys("Hi! Kazi Sifat Al Makud")

driver.find_element(By.CLASS_NAME, "send_mess").click()
time.sleep(6)

driver.quit()
