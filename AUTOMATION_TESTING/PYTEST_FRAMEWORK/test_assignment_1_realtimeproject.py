import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_login_demos:
    def test_sauce_demo_login(self):
        driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("problem_user")
        driver.find_element(By.ID,"password").send_keys('secret_sauce')
        driver.find_element(By.ID,"login-button").click()
        time.sleep(5)
        actual_title=driver.title
        print("actual title of the page after successful login:\n",actual_title)
        assert actual_title== "Swag Labs","login Unsuccessful"
        driver.close(5)

    def test_no_ecommerce_login_demo(self):
        driver = webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F%2F")
        driver.find_element(By.ID, "Email").send_keys("erukulahari129@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("nop@123")
        time.sleep(3)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button').click()
        time.sleep(5)
        print("actual title of the page after successful login:\n",actual_title)
        assert actual_title=="nop commerce", "login Unsuccessful"
        driver.close(5)

    def test_facebook_login_demo(self):
        driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.facebook.com/")
        driver.find_element(By.NAME, "email").send_keys("HARI ERUKULA")
        driver.find_element(By.NAME, "pass").send_keys("Hari@2002")
        driver.find_element(By.NAME, "login").click()
        time.sleep(8)
        print("actual title of the page after successful login:\n",actual_title)
        assert actual_title==" facebook ", "login Unsuccessful"
        driver.close(8)

    def test_instagram_login_demo(self):
        driver = webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.instagram.com/")
        time.sleep(4)
        driver.find_element(By.NAME, "username").send_keys("_krish_na_7")
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("Hari@307")
        time.sleep(4)
        # code to find login button to click to login
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(8)
        print("actual title of the page after successful login:\n", actual_title)
        assert actual_title == " instagram ", "login Unsuccessful"
        driver.close(8)

    def test_hrm_login_demo(self):
        driver = webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        # code to find login button to click to login
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time>sleep(5)
        print("actual title of the page after successful log:\n",actual_title)
        assert actual_title == " orange hrm ", "login Unsuccessful"
        driver.close(8)

    def test_naukri_login_demo(self):
        driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.naukri.com/nlogin/login")
        driver.find_element(By.XPATH, "//input[@id='usernameField']").send_keys("vmurahari324@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='passwordField']").send_keys("Junnu@2003")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(8)
        print("actual title of the page after successful log:\n", actual_title)
        assert actual_title == " naukari  ", "login Unsuccessful"
        driver.close(8)