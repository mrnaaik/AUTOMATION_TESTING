from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
#Load desired web page to be test
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#WRITE A CODE TO LOCATE WEB ELEMENT ON WHICH U WANT TO CLICK
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
#WRITE A CODE TO SWITCH FROM CURRENT MAIN WINDOW TO ALERT WINDOW OR POP UP WINDOW
alert_window=driver.switch_to.alert
time.sleep(5)
print(alert_window.text)
#if u want to accept alert window, with in which any input need to be pass
alert_window.send_keys("sujith@gmail.com")
time.sleep(5)
alert_window.accept() #it means that click on OK Button
#if u want cancel alert window use dismiss() method
#alert_window.dismiss() #it indicates that click on cancel button
time.sleep(5)
#WRITE A CODE TO LOCATE WEB ELEMENT ON WHICH U WANT TO CLICK
driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
#WRITE A CODE TO SWITCH FROM CURRENT MAIN WINDOW TO ALERT WINDOW OR POP UP WINDOW
alert_window=driver.switch_to.alert
time.sleep(5)
alert_window.accept() #IT MEANS THAT CLICK ON OK BUTTON
time.sleep(5)
#WRITE A CODE TO LOCATE WEB ELEMENT ON WHICH U WANT TO CLICK
driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button").click()
#WRITE A CODE TO SWITCH FROM CURRENT MAIN WINDOW TO ALERT WINDOW OR POP UP WINDOW
alert_window=driver.switch_to.alert
time.sleep(5)
alert_window.accept() #IT MEANS THAT CLICK ON OK BUTTON
time.sleep(5)
driver.close()