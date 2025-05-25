from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Edge("c:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
driver.maximize_window()
#locate reference point or intersect point where minimun slider located
min_slider_position=driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a")

max_slider_position=driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[1]")
print("below are the current positions of min and max sliders\n")
print(min_slider_position.location)
print(max_slider_position.location)
time.sleep(5)
#create an object to move min slider to the RHS by adding value in terms of pixels
#such way that current value 107+given value
act.drag_and_drop_by_offset(min_slider_position,8,0).perform()
time.sleep(4)
act.drag_and_drop_by_offset(max_slider_position,-8,0).perform()

time.sleep(5)
print(min_slider_position.location)
print(max_slider_position.location)

