from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
#code to find login button to click to login
driver.find_element(By.XPATH,"//button[@type='submit']").click()

