import logging
from Page_Object_Model.src.pages.Locators.MyAccountSignedOut_locators import MyAccountSignedOutLocators
from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.helpers.config_helpers import add_base_url
import logging as loger
import allure


class MyAccountSignedOut(MyAccountSignedOutLocators):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step('Go to My account page')
    def go_to_my_account(self):
        base_url = add_base_url()
        account_url = base_url + self.endpoint
        logging.info(f'Going to: {account_url}')
        self.driver.get(account_url)

    @allure.step('Input Username to Login')
    def input_login_username(self, username):
        self.sl.wait_and_input_text(username, self.LOGIN_USERNAME)

    @allure.step('Input Email to Register')
    def input_register_email(self, email):
        self.sl.wait_and_input_text(email, self.REGISTER_USERNAME)

    @allure.step('Input Password to Login')
    def input_login_password(self, password):
        self.sl.wait_and_input_text(password, self.LOGIN_PASSWORD)

    @allure.step('Input Password to Register')
    def input_register_password(self, password):
        self.sl.wait_and_input_text(password, self.REGISTER_PASSWORD)

    @allure.step('Click Log in button')
    def click_log_in_button(self):
        logging.debug("Click login button")
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    @allure.step('Click Register  button')
    def click_register_button(self):
        logging.debug("Click login button")
        self.sl.wait_and_click(self.REGISTER_BUTTON)

    @allure.step('Check error message when using invalid credentiaals')
    def verify_error_message(self, error_text):
        self.sl.wait_until_element_contains_text(self.ERROR_MESSAGE, error_text)
