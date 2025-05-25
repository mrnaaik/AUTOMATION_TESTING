from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Edge("c:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://demo.automationtesting.in/Slider.html")
driver.maximize_window()
#locate reference point or intersect point where minimun slider located
min_slider_position=driver.find_element(By.XPATH,"//a[contains(@class,'ui-slider-handle')]")
print("below are the current positions of min slider\n")
print(min_slider_position.location)
time.sleep(5)
#create an object to move min slider to the RHS by adding value in terms of pixels
#such way that current value 107+given value
act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider_position,100,0).perform()
print("after moved position from Min slider\n")
print(min_slider_position.location)
driver.close()
