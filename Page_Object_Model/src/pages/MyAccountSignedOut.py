import logging
from Page_Object_Model.src.pages.Locators.MyAccountSignedOut_locators import MyAccountSignedOutLocators
from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.helpers.config_helpers import add_base_url
import logging as loger


class MyAccountSignedOut(MyAccountSignedOutLocators):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = add_base_url()
        account_url = base_url + self.endpoint
        logging.info(f'Going to: {account_url}')
        self.driver.get(account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_USERNAME, email)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_log_in_button(self):
        logging.debug("Click login button")
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def click_register_button(self):
        logging.debug("Click login button")
        self.sl.wait_and_click(self.REGISTER_BUTTON)

    def verify_error_message(self, error_text):
        self.sl.wait_until_error_message_is_displayed(self.ERROR_MESSAGE, error_text)
