#HANDLING MULTI WINDOWS (PARENT AND CHILD WINDOWS)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#load driver
driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
#load URL on which u want to test
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
#WHILE HANDLING MULTI WINDOWS, each window is assigned with a unique Window ID
window_id=driver.current_window_handle
print(window_id)
driver.find_element(By.XPATH,"//a[@target='_blank']").click()
time.sleep(5)
window_ids=driver.window_handles #returns multiple Windows ID'S generated from the current window
#APPROACH1: how to get all WINDOWS id's generated for inherited windows
parent_window_id=window_ids[0]
child_window_id=window_ids[1]
print(parent_window_id)
print(child_window_id)
#u want to switch parent window
driver.switch_to.window(parent_window_id)
print("parent window after switching back to the parent from child")
print("title of the parent window page",driver.title)
driver.switch_to.window(child_window_id)
print("child page title:",driver.title)
#method2:
'''for w in window_ids:
    driver.switch_to.window(w)
    print(driver.title)
time.sleep(5)'''