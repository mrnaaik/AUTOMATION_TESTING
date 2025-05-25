from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.youtube.com/")
time.sleep(5)
driver.find_element(By.NAME,"search_query").send_keys("ALLU ARJUN")
time.sleep(3)
driver.find_element(By.ID,"search-icon-legacy").click()
time.sleep(5)


