import pytest
from selene import browser
from selenium import webdriver




@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/todomvc/dist/'
    browser.config.driver_name = 'firefox'
    browser.config.driver_options = webdriver.FirefoxOptions()

    yield

    browser.quit()  # closing browser