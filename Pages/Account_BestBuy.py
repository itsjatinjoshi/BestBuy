from selenium.webdriver.common.by import By


class Account:
    account = (By.CSS_SELECTOR, "span[class='accountLabel_20Gjt accountLabel_1cNyz']")
    user_id = (By.CSS_SELECTOR, "input[type='email']")
    user_password = (By.CSS_SELECTOR, 'input[type="password"]')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, driver):
        self.driver = driver

    def get_account_link(self):
        return self.driver.find_element(*Account.account)

    def get_user_id(self):
        return self.driver.find_element(*Account.user_id)

    def get_user_password(self):
        return self.driver.find_element(*Account.user_password)

    def get_submit_button(self):
        return self.driver.find_element(*Account.submit_button)
