from selenium import webdriver
from selenium.webdriver.common.by import By
import time

credentials = [

    {"email": "incorrect@gmail.com", "password": "wrongpass"},
    {"email": "sifat@gmail.com", "password": "123"},

]

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the localhost URL
driver.get("http://localhost/gshop/home.php")
driver.maximize_window()

for cred in credentials:
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
    email_field.send_keys(cred["email"])

    # Fill in the password
    time.sleep(3)
    password_field = driver.find_element(By.CLASS_NAME, "pass")
    password_field.click()
    password_field.send_keys(cred["password"])
    time.sleep(3)

    # Click the submit button
    submit_button = driver.find_element(By.CLASS_NAME, "loginsub")
    submit_button.click()
    time.sleep(3)

    # Click the user button again
    driver.find_element(By.ID, "user-btn").click()
    time.sleep(3)

# Close the browser (optional)
driver.quit()
