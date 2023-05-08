import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os
import pytest_html
import allure


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'firefox', 'ff', 'headlesschrome', 'headlessfirefox']
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
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('headlessfirefox'):
        ff_options = FFOptions()
        ff_options.add_argument('--disable-gpu')
        ff_options.add_argument('--no-sandbox')
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(options=ff_options)

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                # results_dir = os.environ.get("RESULTS_DIR")
                results_dir = "C:/Users/Family/SeleniumPractice/Page_Object_Model/Page_Object_Model/allure_results"
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set")

                screenshot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs["request"]
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
