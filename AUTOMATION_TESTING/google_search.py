from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.google.co.in/")
time.sleep(5)
driver.find_element(By.ID,"APjFqb").send_keys("ALLU ARJUN")
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div/span/svg').click()
time.sleep(5)
