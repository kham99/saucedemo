import time
from pages.authorization_page import AuthPage
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="function")
def auth_fixture(driver):
    auth_page = AuthPage(driver, 'https://www.saucedemo.com/')
    auth_page.open_page()
    auth_page.enter_username('standard_user')
    auth_page.enter_password('secret_sauce')
    auth_page.click_button()
    yield auth_page
    auth_page.driver.quit()

