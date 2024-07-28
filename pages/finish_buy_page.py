from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class CheckOrderFinish(BasePage):
    finish_buy_url = 'https://www.saucedemo.com/checkout-complete.html'

    def __init__(self, driver):
        super().__init__(driver, self.finish_buy_url)

    def open(self):
        super().open()

    def check_successfull_buy(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header')))
        check_header: WebElement = self.driver.find_element(By.CLASS_NAME, 'complete-header')
        assert check_header.text == 'Thank you for your order!'

