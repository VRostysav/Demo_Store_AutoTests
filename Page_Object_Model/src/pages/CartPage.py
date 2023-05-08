from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.helpers.config_helpers import add_base_url
from Page_Object_Model.src.pages.Locators.CartPageLocators import CartPageLocators
import allure


class CartPage(CartPageLocators):
    cart_endpoint = '/cart/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_curt_page(self):
        homepage = add_base_url()
        cart_url = homepage + self.cart_endpoint
        self.driver.get(cart_url)

    @allure.step("Check that selected element is added to curt")
    def get_all_products_names_in_curt(self):
        products_in_curt = self.sl.wait_and_get_elements(self.PRODUCSTS_IN_CURT)
        products_names = [i.text for i in products_in_curt]
        return products_names

    @allure.step("Enter coupon code")
    def enter_coupon_code(self, coupon_code):
        self.sl.wait_and_input_text(coupon_code, self.COUPON_FIELD)

    @allure.step("click Apply coupon")
    def click_apply_coupon_button(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BUTTON)

    @allure.step("verify that coupon applied successfully")
    def get_displayed_message(self):
        message = self.sl.wait_end_get_element_text(self.SUCCESS_MESSAGE)
        return message

    @allure.step("select local pickup shipping")
    def select_local_pickup_radio(self):
        self.sl.wait_and_click(self.LOCAL_PICKUP)

    def aplay_coupon(self, coupon_code):
        self.enter_coupon_code(coupon_code)
        self.click_apply_coupon_button()
        txt = self.get_displayed_message()
        assert txt == 'Coupon code applied successfully.', 'Unexpected message whe applaying coupon'

    @allure.step("click proceed to checkout")
    def click_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEDE_TO_CHECKOUT)


