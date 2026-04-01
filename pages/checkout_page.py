from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page, test_name="checkout_test"):
        super().__init__(page, test_name)

        # Locators
        self.checkout_button = "a.check_out"   # <a class="btn btn-default check_out">Proceed To Checkout</a>
        self.checkout_url = "https://automationexercise.com/checkout"

    # =========================
    # Actions
    # =========================
    def proceed_to_checkout(self):
        self.logger.info("Clicking Proceed To Checkout")
        self.page.locator(self.checkout_button).scroll_into_view_if_needed()
        self.click(self.checkout_button)
        self.page.wait_for_load_state("networkidle")

    # =========================
    # Validations
    # =========================
    def is_checkout_page(self) -> bool:
        return self.page.url.endswith("/checkout") and \
            self.page.is_visible("h2:has-text('Address Details')")


