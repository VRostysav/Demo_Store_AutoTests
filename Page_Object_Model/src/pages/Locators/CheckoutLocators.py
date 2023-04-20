from selenium.webdriver.common.by import By


class CheckoutLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#billing_first_name')
    LAST_NAME = (By.CSS_SELECTOR, '#billing_last_name')
    COUNTRY = (By.CSS_SELECTOR, '#select2-billing_country-results #select2-billing_country-result-81eh-PL')
    COUNTRY_SELECTION_ARROW = (By.CSS_SELECTOR, 'span.select2-selection__arrow')
    STREET_ADDRESS = (By.CSS_SELECTOR, '#billing_address_1')
    CITY = (By.CSS_SELECTOR, '#billing_city')
    # state/country
    POSTCODE = (By.CSS_SELECTOR, '#billing_postcode')
    PHONE = (By.CSS_SELECTOR, '#billing_phone')
    EMAIL = (By.CSS_SELECTOR, '#billing_email')
    PLACE_ORDER = (By.CSS_SELECTOR, '#place_order')
