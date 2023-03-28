import pytest
import time


@pytest.mark.usefixtures('init_driver')
class TestDummy():

    def test_dummy_func(self):
        print('I am dummy test line1')
        print('I am dummy test line2')
        self.driver.get('http://demostore.supersqa.com/')
        time.sleep(3)
