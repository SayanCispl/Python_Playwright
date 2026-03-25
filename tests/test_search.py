import allure
from pages.product_page import ProductPage


@allure.feature("Product")
@allure.story("Search and Add to Cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_and_add_to_cart(page):
    product = ProductPage(page, test_name="test_search_and_add_to_cart")

    with allure.step("Search for Blue Top"):
        product.search_product("Blue Top")

    with allure.step("Add Blue Top to cart"):
        product.add_blue_top_to_cart()

    assert "cart" in page.url.lower(), "Cart page not reached"

    allure.attach(
        page.screenshot(),
        name="Cart after adding Blue Top",
        attachment_type=allure.attachment_type.PNG
    )
