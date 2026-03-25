import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Checkout")
@allure.story("Complete purchase flow")
@allure.severity(allure.severity_level.BLOCKER)
def test_checkout_flow(page):
    # Step 1: Login
    login = LoginPage(page, test_name="checkout_flow")
    with allure.step("Login to account"):
        login.open()
        login.login()
        assert login.is_logged_in(), "Login failed"

    # Step 2: Search product
    product = ProductPage(page, test_name="checkout_flow")
    with allure.step("Search for Blue Top"):
        product.search_product("Blue Top")

    # Step 3: Add to cart
    with allure.step("Add Blue Top to cart"):
        product.add_blue_top_to_cart()

    # Step 4: Validate cart page
    cart = CartPage(page, test_name="checkout_flow")
    with allure.step("Validate cart page"):
        assert cart.is_cart_page(), "Cart page not displayed"

    # Step 5: Proceed to checkout
    checkout = CheckoutPage(page, test_name="checkout_flow")
    with allure.step("Click Proceed to Checkout"):
        checkout.proceed_to_checkout()

    # Step 6: Validate checkout page URL
    with allure.step("Validate checkout page URL"):
        assert checkout.is_checkout_page(), f"Unexpected checkout URL: {page.url}"

    allure.attach(
        page.screenshot(),
        name="Checkout Page",
        attachment_type=allure.attachment_type.PNG
    )
