#radio button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
time.sleep(3)
#driver.find_element(By.ID,"gender-male").click()
driver.find_element(By.ID,"gender-female").click()
time.sleep(2)
#input first name
driver.find_element(By.ID,"FirstName").send_keys("SRINI")
time.sleep(2)
#input lastname
driver.find_element(By.ID,"LastName").send_keys("Midde")
time.sleep(3)
#how to choose date from the dropdown box
day=Select(driver.find_element(By.NAME,"DateOfBirthDay"))
day.select_by_visible_text("10")
time.sleep(3)
#how to choose month from the drop down box
month=Select(driver.find_element(By.NAME,"DateOfBirthMonth"))
month.select_by_visible_text("August")
time.sleep(3)
#how to choose year from the drop down box
year=Select(driver.find_element(By.NAME,"DateOfBirthYear"))
year.select_by_visible_text("2024")
driver.close()