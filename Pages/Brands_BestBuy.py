from selenium.webdriver.common.by import By


class Brands:
    brand_logo = (By.CSS_SELECTOR, "a[class='logoLink_1bLeM']")
    brand_link = (By.CSS_SELECTOR, "span[data-automation='x-brands']")
    brand_sub_links = (By.XPATH, "//div[@class='flyoutMenu_IfVpR active_2JcBh nav-item-brands']/div/ul/li")
    samsung_link = (By.XPATH, "//div[@class='flyoutMenu_IfVpR active_2JcBh nav-item-brands']/div/ul/li[6]/span")
    PQRS_link_internal = (By.XPATH, "//div[@class='brandGroupContainer_1evo2 ']/ul/li")

    samsung = (By.LINK_TEXT, "Samsung")
    samsung_page = (By.CSS_SELECTOR, "h1[class='title_3A6Uh']")

    def __init__(self, driver):
        self.driver = driver

    def get_brand_link(self):
        return self.driver.find_element(*Brands.brand_link)

    def get_brand_sub_link(self):
        return self.driver.find_elements(*Brands.brand_sub_links)

    def get_pqrs_link(self):
        return self.driver.find_elements(*Brands.PQRS_link_internal)

    def get_samsung_link(self):
        return self.driver.find_element(*Brands.samsung_link)

    def get_samsung(self):
        return self.driver.find_element(*Brands.samsung)

    def get_samsung_out(self):
        return self.driver.find_element(*Brands.samsung_page)

    def get_brand_page_logo(self):
        return self.driver.find_element(*Brands.brand_logo)
