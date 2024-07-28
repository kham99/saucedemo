from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    cart_page_url = 'https://www.saucedemo.com/cart.html'

    def __init__(self, driver):
        super().__init__(driver, self.cart_page_url)

    def open(self):
        super().open()

    def check_product_t_shirt(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item_name')))
        t_shirt_title = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name')
        assert t_shirt_title.text == 'Sauce Labs Bolt T-Shirt'

    def buy_product_backpack(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'checkout')))
        backpack = self.driver.find_element(By.ID, 'checkout')
        backpack.click()




