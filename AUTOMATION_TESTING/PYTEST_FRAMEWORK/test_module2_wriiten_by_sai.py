import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_for_url_open:
    def test_method1(self,setup):
        self.driver=setup
        #driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        self.driver.get("https://www.srinisoftwaretraining.com")
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.close()

    def test_method2(self,setup):
        self.driver=setup
        #driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        self.driver.get("https://www.skilltomasters.com")
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.close()
    def test_method3(self,setup):
        self.driver=setup
        #driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        self.driver.get("https://www.nthlearnings.com")
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.close()
    def test_method4(self,setup):
        self.driver=setup
       # driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        self.driver.get("https://www.nativetechhub.com")
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.close()



