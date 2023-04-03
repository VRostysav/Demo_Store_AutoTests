import pytest
from Page_Object_Model.src.pages.MyAccountSignedOut import MyAccountSignedOut
import random


@pytest.mark.usefixtures('init_driver')
class TestRegisterNewUser:
    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_register_email(f'test+{random.randint(1,100)}@test.com')
        # my_account.input_register_password('123_Qwe_123@')
        # my_account.click_register_button()
        # # verify that user is registered

