import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_login_demos:
    def test_sauce_demo_login(self):
        driver=webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("problem_user")
        driver.find_element(By.ID,"password").send_keys('secret_sauce')
        driver.find_element(By.ID,"login-button").click()
        time.sleep(8)
        actual_title=driver.title
        print("actual title of the page after successful login:\n",actual_title)
        assert actual_title==" Swag Labs","login Unsuccessful"
        driver.close()
    def test_no_ecommerce_login_demo(self):
        #driver = webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        #driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
        assert True
        driver.close()
    def test_facebook_login_demo(self):
        #driver = webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        #driver.get("https://www.facebook.com/")
        assert True
        driver.close()
    def test_instagram_login_demo(self):
        #driver = webdriver.Edge("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        #driver.get("https://www.instagram.com/")
        assert True
        driver.close()
    def test_hrm_login_demo(self):

        driver.close()
    def test_naukri_login_demo(self):
        driver.close()


