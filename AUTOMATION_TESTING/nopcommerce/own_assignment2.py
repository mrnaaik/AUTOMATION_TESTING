from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(5)
#driver.find_element(By.ID,"gender-male").click()
driver.find_element(By.ID,"gender-female").click()
time.sleep(2)
#input first name
driver.find_element(By.ID,"FirstName").send_keys("vijaya")
time.sleep(2)
#input lastname
driver.find_element(By.ID,"LastName").send_keys("satvika")
time.sleep(3)
#how to choose date from the dropdown box
day=Select(driver.find_element(By.NAME,"DateOfBirthDay"))
day.select_by_visible_text("20")
time.sleep(3)
#how to choose month from the drop down box
month=Select(driver.find_element(By.NAME,"DateOfBirthMonth"))
month.select_by_visible_text("August")
time.sleep(3)
#how to choose year from the drop down box
year=Select(driver.find_element(By.NAME,"DateOfBirthYear"))
year.select_by_visible_text("2002")
driver.find_element(By.ID,"Email").send_keys("vmurahari324@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"Company").send_keys("cognizant")
time.sleep(3)
driver.find_element(By.ID,"Password").send_keys("123@satvika")
time.sleep(3)
driver.find_element(By.ID,"ConfirmPassword").send_keys("123@satvika")
time.sleep(3)
driver.find_element(By.ID,"register-button").click()
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
