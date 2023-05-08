from Page_Object_Model.src.helpers.config_helpers import add_base_url
from Page_Object_Model.src.pages.Locators.HomeSignOut_locators import HomeSignedOutLocators
from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
import allure


class HomePage(HomeSignedOutLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("Go to home page")
    def go_to_homepage(self):
        homepage = add_base_url()
        self.driver.get(homepage)

    @allure.step("Add item to the curt")
    def click_add_to_curt(self):
        self.sl.wait_and_click_on_random_element(self.ADD_TO_CURT_BUTTON)

    def click_curt_icon(self):
        self.sl.wait_and_click(self.ADD_TO_CURT_BUTTON)
