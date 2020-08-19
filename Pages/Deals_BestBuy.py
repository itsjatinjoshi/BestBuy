from selenium.webdriver.common.by import By


class Deals:
    brand_logo = (By.CSS_SELECTOR, "a[class='logoLink_1bLeM']")
    deals_link = (By.CSS_SELECTOR, "span[data-automation='x-deals']")
    on_sales_week = (By.CSS_SELECTOR, "a[href='/en-ca/collection/shop-all-deals/16074']")
    deals_page = (By.CSS_SELECTOR, "h1[class='title_3A6Uh']")

    def __init__(self, driver):
        self.driver = driver

    def get_deals_link(self):
        return self.driver.find_element(*Deals.deals_link)

    def get_on_sales_week(self):
        return self.driver.find_element(*Deals.on_sales_week)

    def get_hot_deals_text(self):
        return self.driver.find_element(*Deals.deals_page)

    def get_brand_page_logo(self):
        return self.driver.find_element(*Deals.brand_logo)

