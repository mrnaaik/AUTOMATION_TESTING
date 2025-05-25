from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys("9000723703")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("Naik@2001")
#code to find login button to click to login
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
