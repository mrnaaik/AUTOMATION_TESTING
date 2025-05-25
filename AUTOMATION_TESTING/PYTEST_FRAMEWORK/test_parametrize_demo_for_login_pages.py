import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_login_validation:
    @pytest.mark.parametrize("uid,pwd",[("problem_user","secret_sauce"),("problem_user","secret_sauc"),("problem_use","secret_sauce"),("problem_use","secret_sauc")])
    @pytest.mark.skip
    def test_sauce_demo_login(self,uid,pwd):
        driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        driver.find_element(By.ID,"user-name").send_keys(uid)
        time.sleep(3)
        driver.find_element(By.ID,"password").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(5)

    @pytest.mark.parametrize("uid,pwd", [("erukulahari129@gmail.com", "nop@123"), ("erukulahari129@gmail.com", "nop@12"),("erukulahari129@gmail.co", "nop@123"), ("erukulahari129@gmail.co", "nop@12")])
    @pytest.mark.skip
    def test_login_noecomerce_demo(self,uid,pwd):
        driver=webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F%2F")
        driver.maximize_window()
        driver.find_element(By.ID, "Email").send_keys(uid)
        time.sleep(3)
        driver.find_element(By.ID, "Password").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.ID, "RememberMe").click()
        time.sleep(3)
        driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button').click()
        time.sleep(5)

    @pytest.mark.parametrize("uid,pwd", [("9000723703", "Naik@2001"), ("9000765456", "Nak@2001"),("8000723703", "Naik@2002"), ("9000723704", "Naik@2005")])
    def test_login_instagram(self,uid,pwd):
        driver = webdriver.Edge("C:\\Users\\edgedriver_win64\\msedgedriver.exe")
        driver.get("https://www.instagram.com/")
        driver.maximize_window()
        driver.find_element(By.NAME, "username").send_keys(uid)
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys(pwd)
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)