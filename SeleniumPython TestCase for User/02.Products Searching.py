from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the localhost URL
driver.get("http://localhost/gshop/home.php")
driver.maximize_window()

# Define a list of product names to search for
products_to_search = [
    "Hp Victus 16-d0445TX intel i7 11th Gen Laptop Price in BD 2022",
    "ASUS VivoBook S14",
    "Redragon K509 DYAUS 7 Colors Backlit Gaming Keyboard",
    # Add more product names as needed
]

for product in products_to_search:
    # Click the search button
    search_button = driver.find_element(By.CLASS_NAME, "fa-search")
    search_button.click()
    time.sleep(2)
    # Find the search field and perform the search
    search_field = driver.find_element(By.CLASS_NAME, "search_box")
    search_field.click()
    search_field.send_keys(product)
    time.sleep(2)
    # Click the search button again
    search_button = driver.find_element(By.CLASS_NAME, "search_btn")
    search_button.click()

    # Optional: Add a delay to give the page some time to load the results
    time.sleep(2)

# Close the browser (optional)
driver.quit()
