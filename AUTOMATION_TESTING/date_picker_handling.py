from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
#code to switch to the child window as Frame
driver.switch_to_frame(0)
time.sleep(3)
#find date picker as web element
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("10/08/2025")
time.sleep(5)



