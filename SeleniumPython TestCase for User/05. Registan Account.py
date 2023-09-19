from selenium import webdriver
from selenium.webdriver.common.by import By
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
# Click the submit button
submit_button = driver.find_element(By.CLASS_NAME, "regis")
submit_button.click()
time.sleep(3)
name_field = driver.find_element(By.CLASS_NAME, "name1")
name_field.click()
name_field.send_keys("kazi Sifat Al Maksud")
# Fill in the password
time.sleep(3)
email_field = driver.find_element(By.CLASS_NAME, "email")
email_field.click()
email_field.send_keys("sifat@gmail.com")
# Fill in the password
number_field = driver.find_element(By.CLASS_NAME, "number")
number_field.click()
number_field.send_keys("01723903205")
# Fill in the password
time.sleep(3)
password_field = driver.find_element(By.CLASS_NAME, "pass")
password_field.click()
password_field.send_keys("123")
time.sleep(3)

password_field = driver.find_element(By.CLASS_NAME, "repass")
password_field.click()
password_field.send_keys("123")
time.sleep(3)

# Click the user button again
driver.find_element(By.CLASS_NAME, "regitation1").click()

time.sleep(2)
driver.find_element(By.ID, "user-btn").click()
time.sleep(6)
# Close the browser (optional)
driver.quit()
