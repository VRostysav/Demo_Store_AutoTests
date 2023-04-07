from selenium.webdriver.common.by import By


class CartPageLocators:
    COUPON_FIELD = (By.CSS_SELECTOR, '#coupon_code')
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR, 'button[value="Apply coupon"]')
