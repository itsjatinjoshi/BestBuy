import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.fixture(scope="class")
def setup_chrome_browser(request):
    driver = webdriver.Chrome(
        executable_path="C:\\Users\Jatin-PC\Desktop\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.bestbuy.ca/en-ca")
    driver.maximize_window()
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()
