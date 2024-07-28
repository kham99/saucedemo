import pytest
from conftest import auth_fixture
from pages.product_page import ProductPage


@pytest.mark.smoke
def test_filter(auth_fixture):
    filter = ProductPage(auth_fixture.driver)
    filter.open()
    filter.filter_lohi()
