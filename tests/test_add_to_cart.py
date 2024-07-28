import time
import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from conftest import auth_fixture


@pytest.mark.smoke
def test_add_to_cart(auth_fixture):
    product_page = ProductPage(auth_fixture.driver)
    cart_page = CartPage(auth_fixture.driver)
    product_page.open()
    product_page.add_to_cart_t_shirt()
    product_page.click_to_cart()
    cart_page.open()
    cart_page.check_product_t_shirt()




