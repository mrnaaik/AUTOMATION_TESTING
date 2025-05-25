from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,keys
import time
#load driver
driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
#load URL on which u want to test
driver.get("https://www.snapdeal.com/search?keyword=phone&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Price%3A1072%2C5247%7C")
driver.maximize_window()
#LOCATE MINIMUM SLIDER POSITION
min_slider_position=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
max_slider_position=driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
print("current locations or positions of sliders")
print(min_slider_position.location)
print(max_slider_position.location)
#create object for the actionchains
act=ActionChains(driver)
#drag and drop the minimum slider  to the max
act.drag_and_drop_by_offset(min_slider_position,185,0).perform()
time.sleep(4)
act.drag_and_drop_by_offset(max_slider_position,-100,0).perform()

time.sleep(5)
print(min_slider_position.location)
print(max_slider_position.location)
driver.close()