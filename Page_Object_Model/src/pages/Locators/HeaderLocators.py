from selenium.webdriver.common.by import By


class HeaderLocators:
    CART_BUTTON_HEADER = (By.CSS_SELECTOR,'ul.nav-menu li.page-item-7')
    CART_ITEMS_COUNTER = (By.CSS_SELECTOR, 'a.cart-contents span.count')
