import time

import pytest
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="C:\\Users\Jatin-PC\Desktop\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.bestbuy.ca/en-ca")
driver.maximize_window()
driver.find_element_by_css_selector("span[data-automation='x-shop']").click()
shop_link = driver.find_elements_by_xpath("//div[@class='flyoutMenu_IfVpR active_2JcBh nav-item-shop']/div/ul/li")

for s_link in shop_link:
    s_link_name = s_link.find_element_by_xpath("a").text
    print(s_link_name)
    if s_link_name == 'Appliances':
        driver.find_element_by_link_text("Appliances").click()
        time.sleep(4)
        output = driver.find_element_by_css_selector("h1[class='title_3A6Uh']").text
        print(output)
        break

driver.close()
