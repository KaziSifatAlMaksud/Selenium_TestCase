from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the localhost URL
driver.get("http://localhost/gshop/admin/admin_login.php")
driver.maximize_window()

# Define a list of admin users with usernames and passwords
admin_users = [
{"username": "admin2", "password": "222"},
    {"username": "admin3", "password": "333"},
    {"username": "admin", "password": "111"},

    # Add more admin users as needed
]

for admin in admin_users:
    # Fill in the username
    name_field = driver.find_element(By.CLASS_NAME, "name")
    name_field.click()
    name_field.send_keys(admin["username"])
    time.sleep(3)

    # Fill in the password
    email_field = driver.find_element(By.CLASS_NAME, "pass")
    email_field.click()
    email_field.send_keys(admin["password"])
    time.sleep(3)

    # Click the submit button
    driver.find_element(By.CLASS_NAME, "sub").click()
    time.sleep(3)

    # Perform additional actions here, if needed

    # Logout or navigate to another page, for example:
    # driver.get("http://localhost/gshop/admin/some_other_page.php")
    # Perform actions on the other page

# Close the browser (optional)
driver.quit()
