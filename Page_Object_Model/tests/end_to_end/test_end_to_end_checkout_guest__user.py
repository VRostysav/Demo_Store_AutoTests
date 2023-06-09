import pytest
from Page_Object_Model.src.pages.HomePage import HomePage
from Page_Object_Model.src.pages.Header import Header
from Page_Object_Model.src.pages.CartPage import CartPage
from Page_Object_Model.src.pages.CheckoutPage import CheckoutPage
from Page_Object_Model.src.pages.OrderReceivedPage import OrderReceivedPage
from Page_Object_Model.src.configs.generic_configs import GenericConfigs

import time


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGestUser:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_received = OrderReceivedPage(self.driver)
        # go to home page
        home_p.go_to_homepage()
        # add item to the curt
        home_p.click_add_to_curt()
        # make sure that curt is updated before go to it
        header.wait_until_curt_item_count(1)
        # open curt by click curt button
        header.click_on_curt_on_header()
        # chack that selected element is added to curt
        products = cart_page.get_all_products_names_in_curt()
        assert len(products) == 1, f'Expected 1 item in curt but found {len(products)}'
        # enter coupon
        # click add coupon
        # verify that coupon appied succesfully
        coupon_code = GenericConfigs.FREE_COUPON
        cart_page.aplay_coupon(coupon_code)
        # select local pickup shipping
        cart_page.select_local_pickup_radio()
        # click proceed to checkout
        cart_page.click_proceed_to_checkout()
        # fill in form
        checkout_page.filing_billing_information()
        # click place order
        checkout_page.click_place_order()
        # verify order is received
        order_received.verify_order_received_page_loaded()
        order_received.verify_order_number_is_displayed()
