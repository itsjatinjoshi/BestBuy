import inspect

import pytest
import logging

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_chrome_browser")
class BaseClass:

    pass
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
