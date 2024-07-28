import pytest
from conftest import auth_fixture
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.data_filling_form_page import DataForm
from pages.checkout_order_page import CheckOrder
from pages.finish_buy_page import CheckOrderFinish


@pytest.mark.smoke
def test_buy(auth_fixture):
    product = ProductPage(auth_fixture.driver)
    cart = CartPage(auth_fixture.driver)
    form = DataForm(auth_fixture.driver)
    check_order = CheckOrderFinish(auth_fixture.driver)
    button_continue = CheckOrder(auth_fixture.driver)
    product.open()
    product.add_to_cart_backpack()
    product.click_to_cart()
    cart.open()
    cart.buy_product_backpack()
    form.open()
    form.filling_form()
    button_continue.open()
    button_continue.click_finish_button()
    check_order.open()
    check_order.check_successfull_buy()





