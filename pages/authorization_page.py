from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class AuthPage(BasePage):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def open_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="user-name"]')))
        username_field: WebElement = self.driver.find_element(By.XPATH, '//input[@id="user-name"]')
        username_field.send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]')))
        password_field: WebElement = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        password_field.send_keys(password)

    def click_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        button: WebElement = self.driver.find_element(By.XPATH, '//input[@id="login-button"]')
        button.click()






