from Page_Object_Model.src.pages.Locators import MyAccountSignedOut_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MyAccountSignedOut(MyAccountSignedOut_locators):

    def __init__(self, driver):
        self.driver = driver

    def go_to_my_account(self):
        pass

    def input_login_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_USERNAME)).send_keys(username)

    def input_login_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_PASSWORD)).send_keys(password)

    def click_log_in_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BUTTON)).click()

