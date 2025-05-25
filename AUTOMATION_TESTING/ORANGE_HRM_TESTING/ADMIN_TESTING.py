from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace these with your OrangeHRM admin panel credentials
username = "admin"
password = "admin123"

# Start a new instance of Chrome WebDriver
#driver = webdriver.Chrome()
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
# Navigate to OrangeHRM admin login page
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")

driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
#code to find login button to click to login
driver.find_element(By.XPATH,"//button[@type='submit']").click()



# Find username and password input fields and login button
username_input = driver.find_element_by_id("txtUsername")
password_input = driver.find_element_by_id("txtPassword")
login_button = driver.find_element_by_id("btnLogin")

# Fill in the login form and submit
username_input.send_keys(username)
password_input.send_keys(password)
login_button.click()

# Wait for the dashboard page to load
dashboard_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dashboard"))
)

# Now you can automate various tasks on the admin panel

# Example: Click on the Admin tab
admin_tab = driver.find_element_by_id("menu_admin_viewAdminModule")
admin_tab.click()

# Example: Click on the Add button to add a new user
add_button = driver.find_element_by_id("btnAdd")
add_button.click()

# Example: Fill in the form to add a new user
# Replace these with the details you want to fill in
user_name_input = driver.find_element_by_id("systemUser_employeeName_empName")
user_name_input.send_keys("John Doe")

# After filling in the form, you can continue with other actions as needed

# Close the browser session
driver.quit()