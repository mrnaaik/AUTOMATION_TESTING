from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Edge("c:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.snapdeal.com/search?keyword=phone&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Price%3A38%2C5499%7C")
driver.maximize_window()
#locate reference point or intersect point where minimun slider located
min_slider_position=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")

max_slider_position=driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
print("below are the current positions of min and max sliders\n")
print(min_slider_position.location)
print(max_slider_position.location)
time.sleep(5)
#create an object to move min slider to the RHS by adding value in terms of pixels
#such way that current value 107+given value
act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider_position,100,0).perform()
print("after moved position from Min slider\n")
print(min_slider_position.location)
driver.close()
