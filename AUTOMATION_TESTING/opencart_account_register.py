from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME,"firstname").send_keys("vijaya")
time.sleep(5)
driver.find_element(By.NAME,"lastname").send_keys("satvika")
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys("vmurahari324@gmail.com")
time.sleep(5)
driver.find_element(By.NAME,"country_id").send_keys("india")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("vijaya@123")
time.sleep(5)
driver.find_element(By.XPATH,"//a[@class='active']//img").click()
time.sleep(5)


#code to find login button to click to login
driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-lg hidden-xs']").click()
driver.close()