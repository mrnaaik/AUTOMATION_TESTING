from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys("9000723703")
time.sleep(3)
driver.find_element(By.NAME,"pass").send_keys("Naik@2001")
#code to find login button to click to login
driver.find_element(By.NAME,"login").click()