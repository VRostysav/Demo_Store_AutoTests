from Page_Object_Model.src.helpers.config_helpers import add_base_url
from Page_Object_Model.src.SeleniumExtended import SeleniumExtended
from Page_Object_Model.src.pages.Locators.CheckoutLocators import CheckoutLocators
from Page_Object_Model.src.helpers.generic_helpers import generate_random_email_and_password
import allure


class CheckoutPage(CheckoutLocators):
    checkout_endpoint = '/checkout/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_checkout_page(self):
        homepage = add_base_url()
        checkout_url = homepage + self.checkout_endpoint
        self.driver.get(checkout_url)

    def input_first_name(self, first_name='TestFname'):
        self.sl.wait_and_input_text(first_name, self.FIRST_NAME)

    def input_last_name(self, last_name='TestLname'):
        self.sl.wait_and_input_text(last_name, self.LAST_NAME)

    # def select_country_or_region(self):
    #     self.sl.wait_and_click(self.COUNTRY_SELECTION_ARROW)
    #     self.sl.scroll_and_click(self.COUNTRY)

    def input_street_address(self, address='123 Main street'):
        self.sl.wait_and_input_text(address, self.STREET_ADDRESS)

    def input_city(self, city=None):
        city = city if city else 'San Francisco'
        self.sl.wait_and_input_text(city, self.CITY)

    def input_postcode(self, postcode=None):
        postcode = postcode if postcode else '95009'
        self.sl.wait_and_input_text(postcode, self.POSTCODE)

    def input_phone(self, phone=None):
        phone = phone if phone else '4151111111'
        self.sl.wait_and_input_text(phone, self.PHONE)

    def input_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email["email"]
        self.sl.wait_and_input_text(email, self.EMAIL)

    @allure.step("Fill in billing information")
    def filing_billing_information(self):
        self.input_first_name()
        self.input_last_name()
        # self.select_country_or_region()
        self.input_street_address()
        self.input_city()
        self.input_postcode()
        self.input_phone()
        self.input_email()

    @allure.step("Click place order")
    def click_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER)
