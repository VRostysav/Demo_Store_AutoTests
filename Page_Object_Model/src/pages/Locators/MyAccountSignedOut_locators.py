from selenium.webdriver.common.by import By


class MyAccountSignedOutLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.woocommerce-form-login__submit')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'ul.woocommerce-error')
