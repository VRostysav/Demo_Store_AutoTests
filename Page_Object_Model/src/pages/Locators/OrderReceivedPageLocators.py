from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:
    ORDER_TITLE = (By.CSS_SELECTOR, 'h1.entry-title')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')
