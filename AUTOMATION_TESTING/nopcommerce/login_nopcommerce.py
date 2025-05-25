from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Log in").click()
time.sleep(5)
driver.find_element(By.ID,"Email").send_keys("vmurahari324@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"Password").send_keys("123@satvika")
time.sleep(2)
driver.find_element(By.ID,"RememberMe").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

