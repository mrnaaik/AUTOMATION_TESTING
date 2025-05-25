import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
    return driver