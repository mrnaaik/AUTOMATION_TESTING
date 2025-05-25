
#this file consist all testing methods by interacting functional testing
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
import time
#in Fixed_Deposit_Calulator file we want to call XLUtils methods definitions
from AUTOMATION_TESTING.DATA_DRIVEN_TESTING import XLUtils
driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(15)
#locate excell file
file="C:/Users/caldata.xlsx"
#row count
rows=XLUtils.getRowCount(file,"Sheet1")
#READ DATA FROM EXCELL SHEET
for r in range(2,rows+1):
    pric=XLUtils.readData(file,"Sheet1",r,1) #20000
    rateofinterest=XLUtils.readData(file,"Sheet1",r,2) #10
    per1=XLUtils.readData(file,"Sheet1",r,3) #2
    per2=XLUtils.readData(file,"Sheet1",r,4)# years
    fre=XLUtils.readData(file,"Sheet1",r,5)#simple interest
    exp_mvalue=XLUtils.readData(file,"Sheet1",r,6) #24000
#CODE TO pass above to the money control application to conduct functional testing
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    periodrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    periodrp.select_by_visible_text(per2)
    frequencydrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(fre)
#clik calc button
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue=driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text
#validate and verify data result given by application and excell data
    if(float(exp_mvalue)==float(act_mvalue)):
        print("test Passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLUtils.writeData(file,"Sheet1",r,8,"Filed")
        XLUtils.fillRedColor(file,"Sheet1",r,8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)
driver.close()
