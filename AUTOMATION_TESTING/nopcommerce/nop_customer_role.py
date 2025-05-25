from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
# Open the nopCommerce website
driver.get("http://demo.nopcommerce.com/")

# Click on the Register link
register_link = driver.find_element_by_link_text("Register")
register_link.click()

# Fill out the registration form
first_name = driver.find_element_by_id("FirstName")
first_name.send_keys("John")

last_name = driver.find_element_by_id("LastName")
last_name.send_keys("Doe")

email = driver.find_element_by_id("Email")
email.send_keys("john.doe@example.com")

password = driver.find_element_by_id("Password")
password.send_keys("password123")

confirm_password = driver.find_element_by_id("ConfirmPassword")
confirm_password.send_keys("password123")

# Click on the Register button
register_button = driver.find_element_by_id("register-button")
register_button.click()

# Wait for registration to complete
time.sleep(5)

# Check if registration was successful
if "Your registration completed" in driver.page_source:
    print("Registration successful!")
else:
    print("Registration failed.")

# Close the browser
driver.quit()