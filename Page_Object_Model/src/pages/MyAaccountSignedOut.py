from Page_Object_Model.src.pages.Locators import MyAccountSignedOut_locators
from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.helpers.config_helpers import add_base_url


class MyAccountSignedOut(MyAccountSignedOut_locators):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = add_base_url()
        account_url = base_url + self.endpoint
        self.driver.get(account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_log_in_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)
