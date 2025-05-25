''''#demo about use of link_text and link_partial_text web locators

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(8)'''

#demo about use of link_text and link_partial_text web locators

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
#driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
time.sleep(8)