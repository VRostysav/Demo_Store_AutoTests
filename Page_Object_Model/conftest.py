import pytest
from selenium import webdriver
import os


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'firefox', 'ff', 'headlesschrome']
    os.environ['BROWSER'] = 'ch'
    browser = os.environ.get('BROWSER', None)

    if not browser:
        raise Exception('An environment variable BROWSER must be set')

    browser.lower()
    if browser not in supported_browsers:
        raise Exception(f'Provided browser{browser} is not one of the supported')

    if browser in ('ch', 'chrome'):
        driver = webdriver.Chrome()
    elif browser in ('ff', 'firefox'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    #driver.quit()
