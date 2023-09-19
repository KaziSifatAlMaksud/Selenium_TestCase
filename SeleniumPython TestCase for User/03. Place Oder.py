from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the localhost URL
driver.get("http://localhost/gshop/home.php")
driver.maximize_window()

# Click the user button
driver.find_element(By.ID, "user-btn").click()

# Find all <p> elements on the page
paragraphs = driver.find_elements(By.TAG_NAME, "p")

# Loop through each <p> element and check its text
for p in paragraphs:
    if p.text == "please login first!":
        # Click the login button
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        login_button.click()
        break  # Exit the loop
# Fill in the email
time.sleep(3)
email_field = driver.find_element(By.CLASS_NAME, "email")
email_field.click()
email_field.send_keys("sifat@gmail.com")
# Fill in the password
password_field = driver.find_element(By.CLASS_NAME, "pass")
password_field.click()
password_field.send_keys("123")
# Click the submit button
submit_button = driver.find_element(By.CLASS_NAME, "loginsub")
submit_button.click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "obtn").click()
time.sleep(3)
# Click the user button
driver.find_element(By.CLASS_NAME, "card_btn").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, "oder_btn").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "oderr_btn").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "obtn").click()
time.sleep(3)
driver.quit()
