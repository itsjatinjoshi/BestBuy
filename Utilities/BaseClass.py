import inspect

import pytest
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup_chrome_browser")
class BaseClass:

    def best_buy_home_logo(self, brand_logo):
        brand_log = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, brand_logo))) #"a[class='logoLink_1bLeM']"
        # return self.brand_log.click()




    # pass
    # def test_logging_demo(self):
    #     logger_name = inspect.stack()[1][3]
    #     logger = logging.getLogger(logger_name)
    #     file_handler = logging.FileHandler("logfile.log")
    #     formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #     file_handler.setFormatter(formatter)
    #     logger.addHandler(file_handler)
    #
    #     logger.setLevel(logging.INFO)
    #     return logger
