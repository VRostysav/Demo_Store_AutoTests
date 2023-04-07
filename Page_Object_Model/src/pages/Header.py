from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.pages.Locators.HeaderLocators import HeaderLocators


class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_curt_on_header(self):
        self.sl.wait_and_click(self.CART_BUTTON_HEADER)

    def wait_until_curt_item_count(self, count):
        expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.CART_ITEMS_COUNTER, expected_text)
