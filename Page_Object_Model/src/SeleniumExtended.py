from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, text, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout). \
            until(EC.visibility_of_element_located(locator)).click()

    def wait_until_error_message_is_displayed(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_and_click_on_random_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        list_of_elems = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        random.choice(list_of_elems).click()
