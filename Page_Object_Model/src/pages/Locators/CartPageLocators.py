from selenium.webdriver.common.by import By


class CartPageLocators:
    COUPON_FIELD = (By.CSS_SELECTOR, '#coupon_code')
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR, 'button[value="Apply coupon"]')
    PRODUCSTS_IN_CURT = (By.CSS_SELECTOR, 'tr.cart_item > td.product-name')
    PROCEDE_TO_CHECKOUT = (By.CSS_SELECTOR, 'div.wc-proceed-to-checkout a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.woocommerce-message')
    LOCAL_PICKUP = (By.CSS_SELECTOR, '#shipping_method_0_local_pickup3')