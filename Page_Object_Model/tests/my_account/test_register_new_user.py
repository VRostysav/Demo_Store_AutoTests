import pytest
from Page_Object_Model.src.pages.MyAccountSignedOut import MyAccountSignedOut
from Page_Object_Model.src.pages.MyAccountSignedIn import MyAccountSignedIn
from Page_Object_Model.src.helpers.generic_helpers import generate_random_email_and_password
import random


@pytest.mark.usefixtures('init_driver')
class TestRegisterNewUser:
    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account.go_to_my_account()

        random_email = generate_random_email_and_password()
        my_account.input_register_email(random_email["email"])
        my_account.input_register_password('1234abc')
        my_account.click_register_button()

        # # verify that user is registered
        my_account_i.verify_user_is_signed_in()

