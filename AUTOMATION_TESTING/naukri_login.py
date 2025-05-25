from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.naukri.com/nlogin/login")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='usernameField']").send_keys("vmurahari324@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='passwordField']").send_keys("Junnu@2003")
#code to find login button to click to login
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.naukri.com/nlogin/login")
time.sleep(5)
driver.find_element(By.ID,"usernameField").send_keys("vmurahari324@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"passwordField").send_keys("Junnu@2003")
#code to find login button to click to login
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()'''