import pytest
from Page_Object_Model.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        # my_account.input_login_username('dadasda')
        # my_account.input_login_password('sadadasSDA21')
        my_account.click_log_in_button()
        error_text = 'Error: Username is required.'
        my_account.verify_error_message(error_text)






