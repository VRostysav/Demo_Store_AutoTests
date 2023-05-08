from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.helpers.config_helpers import add_base_url
from Page_Object_Model.src.pages.Locators.OrderReceivedPageLocators import OrderReceivedPageLocators
import allure


class OrderReceivedPage(OrderReceivedPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    @allure.step("verify order is received")
    def verify_order_received_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.ORDER_TITLE, 'Order received')

    def verify_order_number_is_displayed(self):
       return self.sl.wait_end_get_element_text(self.ORDER_NUMBER)
