from pages.base_page import BasePage
from config.settings import Settings


class CartPage(BasePage):
    def __init__(self, page, test_name="cart_test"):
        super().__init__(page, test_name)
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"
        self.view_cart_in_modal = "#cartModal .modal-footer a[href='/view_cart']"
        self.cart_modal = "#cartModal"
        self.cart_page_identifier = "#cart_info table"

    def navigate(self):
        self.logger.info("Navigating to shop page")
        self.page.goto(Settings.SHOP_URL)  # ✅ use class attribute directly
        self.page.wait_for_load_state("networkidle")

    def add_item_to_cart(self):
        self.logger.info("Adding item to cart")
        self.page.locator(self.add_to_cart_button).scroll_into_view_if_needed()

        try:
            self.click(self.add_to_cart_button)
        except Exception:
            self.logger.warning("Standard click failed, using JS click fallback")
            self.page.locator(self.add_to_cart_button).evaluate("el => el.click()")

        self.handle_cart_modal()

        if not self.is_cart_page():
            raise AssertionError(f"Not on cart page. URL: {self.page.url}")

    def handle_cart_modal(self):
        self.logger.info("Handling cart modal")

        try:
            self.page.wait_for_selector(
                self.cart_modal,
                state="visible",
                timeout=8000
            )
            self.logger.info("Cart modal appeared")
            self.page.locator(self.view_cart_in_modal).click(timeout=5000)

        except Exception as e:
            self.logger.warning(f"Modal approach failed: {e}, trying direct navigation")
            self.page.goto(f"{Settings.BASE_URL}/view_cart")

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector(self.cart_page_identifier, timeout=15000)

    def is_cart_page(self) -> bool:
        try:
            self.page.wait_for_selector(self.cart_page_identifier, timeout=5000)
            return "/view_cart" in self.page.url
        except Exception:
            return False