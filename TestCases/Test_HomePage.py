import time

from Pages.Home_BestBuy import Home
from Utilities.BaseClass import BaseClass


class TestBestBuyHome(BaseClass):
    def test_homepage(self):
        home = Home(self.driver)
        # home.get_home_page_logo().click()
        home.get_shop_link().click()

        shop_link = home.get_shop_sub_link()
        for s_link in shop_link:
            s_link_name = s_link.find_element_by_xpath("a").text
            print("Link Name: ", s_link_name)
            if s_link_name == 'Appliances':
                home.get_appliances_link().click()
                # print(self.driver.title)
                # time.sleep(4)
                # appliance_window = self.driver.window_handles("Appliances")
                # self.driver.switch_to.window(appliance_window)
                time.sleep(4)
                output = home.get_appliances_output_text().text
                print(output)
                assert output == "Appliances"
                break

        home.get_home_page_logo().click()
