from selenium.webdriver.common.by import By


class HomeSignedOutLocators:
    ADD_TO_CURT_BUTTON = (By.CSS_SELECTOR, 'ul.columns-4 li >a.add_to_cart_button')
    CURT_BUTTON_WITH_PICTURE = (By.CSS_SELECTOR, 'a.cart-contents')
