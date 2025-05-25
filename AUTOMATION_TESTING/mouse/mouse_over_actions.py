from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.ebay.com/")

driver.maximize_window()
#find an element on which u want to apply mouse over action
electronics=driver.find_element(By.XPATH,"//*[@id='vl-flyout-nav']/ul/li[3]/a")
act=ActionChains(driver)
time.sleep(3)
act.move_to_element(electronics).click().perform()
time.sleep(5)
