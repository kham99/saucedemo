from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class CheckOrder(BasePage):
    check_order_url = 'https://www.saucedemo.com/checkout-step-two.html'

    def __init__(self, driver):
        super().__init__(driver, self.check_order_url)

    def open(self):
        super().open()

    def click_finish_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'finish')))
        button_finish: WebElement = self.driver.find_element(By.ID, 'finish')
        button_finish.click()

