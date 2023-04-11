from Page_Object_Model.src.pages.Locators import  HomeSignOut_locators
from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.helpers.config_helpers import add_base_url
from Page_Object_Model.src.pages.Locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):
    cart_endpoint = '/cart/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_curt_page(self):
        homepage = add_base_url()
        cart_url = homepage + self.cart_endpoint
        self.driver.get(cart_url)

    def get_all_products_names_in_curt(self):
        products_in_curt = self.sl.wait_and_get_elements(self.PRODUCSTS_IN_CURT)
        products_names = [i.text for i in products_in_curt]
        return products_names

    def enter_coupon_code(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)

    def click_apply_coupon_button(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BUTTON)

    def aplay_coupon(self, coupon_code):
        self.enter_coupon_code(coupon_code)
        self.click_apply_coupon_button()
