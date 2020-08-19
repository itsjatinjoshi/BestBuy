import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from Pages.Deals_BestBuy import Deals
from Pages.Home_BestBuy import Home
from Pages.Brands_BestBuy import Brands
from Utilities.BaseClass import BaseClass
from Pages.Account_BestBuy import Account


class TestBestBuyHome(BaseClass):

    def test_home_page(self):
        home = Home(self.driver)
        # home.get_home_page_logo().click()
        self.best_buy_home_logo("a[class='logoLink_1bLeM']")
        home.get_shop_link().click()

        shop_link = home.get_shop_sub_link()
        for s_link in shop_link:
            s_link_name = s_link.find_element_by_xpath("a").text
            print("Link Name: ", s_link_name)
            if s_link_name == 'Appliances':
                home.get_appliances_link().click()
                time.sleep(4)
                output = home.get_appliances_output_text().text
                print(output)
                assert output == "Appliances"
                break

        # home.get_home_page_logo().click()
        self.best_buy_home_logo("a[class='logoLink_1bLeM']")
        time.sleep(4)

    def test_brand_page(self):

        brand_page = Brands(self.driver)
        brand_page.get_brand_link().click()

        brands = brand_page.get_brand_sub_link()
        for brand in brands:
            brand_names = brand.find_element_by_xpath('span').text
            if brand_names == "P Q R S":

                add = brand_page.get_samsung_link()

                action = ActionChains(self.driver)
                action.move_to_element(add).perform()
                submenu = wait(self.driver, 10).until(EC.element_to_be_clickable(brand_page.samsung_link))
                submenu.click()

                pqrs = brand_page.get_pqrs_link()
                # time.sleep(3)
                for sam in pqrs:
                    sub_brand_name = sam.find_element_by_xpath("a").text
                    if sub_brand_name == "Samsung":
                        brand_page.get_samsung().click()
                        time.sleep(4)
                        output = brand_page.get_samsung_out().text

                        assert "Samsung" == output
                        break

                # brand_page.get_brand_page_logo().click()
                self.best_buy_home_logo("a[class='logoLink_1bLeM']")
                time.sleep(4)
                break

    def test_deals(self):

        deals = Deals(self.driver)

        deals.get_deals_link().click()
        deals.get_on_sales_week().click()

        time.sleep(4)

        deals_page_text = deals.get_hot_deals_text().text

        assert deals_page_text == "Hot Deals"
        self.best_buy_home_logo("a[class='logoLink_1bLeM']")
        # deals.get_brand_page_logo().click()
        time.sleep(4)

    def test_account(self):
        account = Account(self.driver)
        account.get_account_link().click()
        # time.sleep(10)

        wait(self.driver, 10).until(EC.presence_of_element_located(account.user_id))
        wait(self.driver, 10).until(EC.presence_of_element_located(account.user_password))

        account.get_user_id().send_keys(input("email: "))
        account.get_user_password().send_keys("Password: ")
        account.get_submit_button().click()