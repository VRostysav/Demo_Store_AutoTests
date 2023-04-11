from selenium.webdriver.common.by import By


class CartPageLocators:
    COUPON_FIELD = (By.CSS_SELECTOR, '#coupon_code')
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR, 'button[value="Apply coupon"]')
    PRODUCSTS_IN_CURT = (By.CSS_SELECTOR, 'tr.cart_item > td.product-name')
