from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class ProductPage(BasePage):
    product_page_url = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        super().__init__(driver, self.product_page_url)

    def open(self):
        super().open()

    def add_to_cart_t_shirt(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        product_button: WebElement = self.driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        product_button.click()

    def click_to_cart(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link')))
        cart_button = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_button.click()

    def add_to_cart_backpack(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-backpack')))
        cart_button = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        cart_button.click()


    def filter_lohi(self):
        original_products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        self.driver.find_element(By.CLASS_NAME, "product_sort_container").click()
        self.driver.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()
        new_products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        original_product_titles = [product.find_element(By.CLASS_NAME, "inventory_item_name").text for product in
                                   original_products]
        new_product_titles = [product.find_element(By.CLASS_NAME, "inventory_item_name").text for product in
                              new_products]
        expected_product = 'Sauce Labs Onesie'
        assert expected_product in original_product_titles, f"{expected_product} was not found in the original product list."
        expected_position = new_product_titles.index(expected_product)
        assert expected_position == 0, (f"Expected '{expected_product}' to be at position 1 but found it at position "
                                        f"{expected_position + 1}.")
