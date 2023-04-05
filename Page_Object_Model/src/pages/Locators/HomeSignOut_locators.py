from selenium.webdriver.common.by import By


class HomeSignedOutLocators:
    PRODUCTS = (By.CSS_SELECTOR, 'products columns-4')
    CURT_BUTTON_WITH_PICTURE = (By.CSS_SELECTOR, 'a.cart-contents')
