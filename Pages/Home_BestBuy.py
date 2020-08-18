import time

from selenium.webdriver.common.by import By


class Home:
    home_page = (By.CSS_SELECTOR, "a[class='logoLink_1bLeM']")
    shop_link = (By.CSS_SELECTOR, "span[data-automation='x-shop']")
    shop_sub_link = (By.XPATH, "//div[@class='flyoutMenu_IfVpR active_2JcBh nav-item-shop']/div/ul/li")
    appliance_link = (By.LINK_TEXT, "Appliances")
    output_text = (By.CSS_SELECTOR, "h1[class='title_3A6Uh]'")

    def __init__(self, driver):
        self.driver = driver

    def get_home_page_logo(self):
        return self.driver.find_element(*Home.home_page)

    def get_shop_link(self):
        return self.driver.find_element(*Home.shop_link)

    def get_shop_sub_link(self):
        return self.driver.find_elements(*Home.shop_sub_link)

    def get_appliances_link(self):
        return self.driver.find_element(*Home.appliance_link)

    def get_appliances_output_text(self):
        return self.driver.find_element(*Home.output_text)
