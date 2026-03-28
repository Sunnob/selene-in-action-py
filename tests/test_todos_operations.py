from multiprocessing.context import assert_spawning

from selene import browser, have, be, by
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_complete_todo():
    browser.open('/') #opening browser
    browser.element('.new-todo').should(be.blank)
    browser.driver.find_element(By.CSS_SELECTOR, '.new-todo')

    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('.todo-list>li').with_(timeout=browser.config.timeout * 1.5).should(have.size(3))

    browser.all('.todo-list>li').should(have.size(3))  # selene
    # browser.all('.todo-list>li').wai.for_(have.size(3))


    '''
    assert len(browser.driver.find_elements(*by.css('.todo-list>li'))) == 3
    WebDriverWait(driver=browser.driver,timeout=3.0).until(lambda driver: len(driver.find_elements(*by.css('.todo-list>li'))) == 3) #selenium webdriver
    '''

# def test_complete_todo2(driver, browser):
#
#    driver.get('https://todomvc.com/examples/emberjs/todomvc/dist/')
#    iniatial_value = browser.element('.new-todo').locate()
#    assert_driver.find_element(*by.css('.new-todo')).get_attribute('value') == ''
#
#    browser.element('.new-todo').send_keys('a' + Keys.ENTER)
#    driver.find_element(*by.css('.new-todo')).send_keys('b' + Keys.ENTER)
#    driver.find_element(*by.css('.new-todo')).send_keys('c' + Keys.ENTER)
