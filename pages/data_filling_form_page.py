from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class DataForm(BasePage):
    product_page_url = 'https://www.saucedemo.com/checkout-step-one.html'

    def __init__(self, driver):
        super().__init__(driver, self.product_page_url)

    def open(self):
        super().open()

    def filling_form(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'first-name')))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'last-name')))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'postal-code')))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'continue')))
        firstname: WebElement = self.driver.find_element(By.ID, 'first-name')
        firstname.send_keys('Amir')
        lastname: WebElement = self.driver.find_element(By.ID, 'last-name')
        lastname.send_keys('Khabiev')
        postal_code: WebElement = self.driver.find_element(By.ID, 'postal-code')
        postal_code.send_keys('999')
        button_continue: WebElement = self.driver.find_element(By.ID, 'continue')
        button_continue.click()
