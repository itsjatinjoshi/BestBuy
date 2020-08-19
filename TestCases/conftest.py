import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup_chrome_browser(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\Jatin-PC\Desktop\Drivers\chromedriver_win32\chromedriver.exe")

    elif browser_name == "firefox":
        # set path of firefox with gecko driver
        pass
    elif browser_name == "IE":
        # set the path of IE driver
        pass

    driver.get("https://www.bestbuy.ca/en-ca")
    driver.maximize_window()
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()
