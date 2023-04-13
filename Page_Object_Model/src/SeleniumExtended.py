import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException
import random


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, text, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout). \
            until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout). \
                until(EC.visibility_of_element_located(locator)).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_and_get_elements(self, locator, timeout=None, error=None):
        timeout = timeout if timeout else self.default_timeout
        error = error if error else f"Unable to find elements by {locator}," \
                                    f"after timeout {timeout}"
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(error)
        return  elements

    def wait_and_click_on_random_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        list_of_elems = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        random.choice(list_of_elems).click()

    def wait_end_get_element_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait.until(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element_text = element.text
        return element_text
