import pytest
from selene import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # 1. Selene Settings
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/todomvc/dist/'
    browser.config.timeout = 2.0

    # 2. Driver Settings (Исправлено на ChromeOptions!)
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')

    # 3. Created driver and give it to Selene (Создаем драйвер и отдаем его под управление Selene)
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )

    yield

    # 4. Закрываем браузер
    browser.quit()
