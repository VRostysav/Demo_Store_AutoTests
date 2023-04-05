import pytest
from Page_Object_Model.src.pages.HomePage import HomePage
import time

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGestUser:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_p=HomePage(self.driver)
        #go to home page
        home_p.go_to_homepage()
        # add item to the curt
        home_p.click_add_to_curt()
        time.sleep(6)
        #open curt by click curt button
        #enter coupon
        #click add coupon
        #chacke price after applying coupon
        # click proceed to checkout
        # fill in form
        #click place order
        #verify order is received





