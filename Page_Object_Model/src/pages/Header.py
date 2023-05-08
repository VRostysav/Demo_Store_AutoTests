from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.pages.Locators.HeaderLocators import HeaderLocators
import allure


class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("Curt item counter is updated")
    def wait_until_curt_item_count(self, count):
        expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.CART_ITEMS_COUNTER, expected_text)

    @allure.step("Open curt by click curt button")
    def click_on_curt_on_header(self):
        self.sl.wait_and_click(self.CART_BUTTON_HEADER)
