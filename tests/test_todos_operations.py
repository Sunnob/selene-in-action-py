from selene import browser, have, be
from selenium.webdriver.common.by import By

def test_complete_todo():
    browser.open('/') #opening browser
    browser.element('.new-todo').should(be.blank)
    browser.driver.find_element(By.CSS_SELECTOR, '.new-todo')

    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('.todo-list>li').should(have.size(3))