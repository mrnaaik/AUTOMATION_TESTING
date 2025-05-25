from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("admin123")
#code to find login button to click to login
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/svg").click()



'''driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
#code to find login button to click to login
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()'''

