from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(3)
driver.find_element(By.ID,"product_549").click()
time.sleep(3)
driver.find_element(By.ID,"travname").send_keys("VIJAYA")
time.sleep(3)
driver.find_element(By.ID,"travlastname").send_keys("SATVIKA")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='dob']").send_keys("10/08/2025")
time.sleep(5)
driver.find_element(By.ID,"sex_2").click()
time.sleep(3)
driver.find_element(By.ID,"addmorepax").click()
time.sleep(3)
passenger=Select(driver.find_element(By.ID,"select2-addpaxno-container"))
day.select_by_visible_text("add 1 more passenger (100%)")







