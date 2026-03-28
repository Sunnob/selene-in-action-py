import pytest
from selene import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/todomvc/dist/'
    browser.config.timeout = 2.0
    driver_options = webdriver.FirefoxOptions()
    driver_options.add_argument('--headless=new')
    # browser.config.driver_options = driver_options
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )

    yield

    browser.quit()  # closing browser

@pytest.fixture()
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )

    yield driver
    driver.quit()


@pytest.fixture()
def browser(driver):

    yield Browser(Config(driver=driver))