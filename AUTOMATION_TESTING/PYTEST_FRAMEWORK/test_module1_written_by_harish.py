import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_for_url_open:
    def test_method1(self):
        driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.srinisoftwaretraining.com")
        driver.maximize_window()
        time.sleep(4)
        driver.close()

    def test_method2(self):
        driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.skilltomasters.com")
        driver.maximize_window()
        time.sleep(4)
        driver.close()
    def test_method3(self):
        driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.nthlearnings.com")
        driver.maximize_window()
        time.sleep(4)
        driver.close()
    def test_method4(self):
        driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.nativetechhub.com")
        driver.maximize_window()
        time.sleep(4)
        driver.close()



