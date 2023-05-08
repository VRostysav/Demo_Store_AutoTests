from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.pages.Locators.MyAccountSignedIn_locators import MyAccountSignedInLocators
import allure


class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("Check that user is signed in")
    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NOV_BAR_LOGOUT_BUTTON)
