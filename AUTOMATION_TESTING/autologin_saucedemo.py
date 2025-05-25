from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#code to locate webdriver in the locaal path
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.saucedemo.com/v1/")
time.sleep(5)
#in login page, write a code to locate user name input box using
#either id as web locator or name as web locator
#if incase id or name not available then use xpath as the web locator
#driver.find_element(By.ID,"user-name").send_keys("problem_user")
driver.find_element(By.NAME,"user-name").send_keys("problem_user")
time.sleep(3)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
#code to find login button to click to login
driver.find_element(By.ID,"login-button").click()
