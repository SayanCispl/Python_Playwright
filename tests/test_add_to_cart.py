import allure
from pages.cart_page import CartPage

@allure.feature("Cart")
@allure.story("Add item to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(page):
    cart = CartPage(page, test_name="test_add_to_cart")

    with allure.step("Navigate to shop page"):
        cart.navigate()

    with allure.step("Add item to cart"):
        cart.add_item_to_cart()

    with allure.step("Validate cart page is visible"):
        assert cart.is_cart_page(), "Cart page not displayed"

    allure.attach(
        page.screenshot(),
        name="Cart Page Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
