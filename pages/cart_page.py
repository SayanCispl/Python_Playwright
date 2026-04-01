from pages.base_page import BasePage
from config.settings import Settings

class CartPage(BasePage):
    def __init__(self, page, test_name="cart_test"):
        super().__init__(page, test_name)

        # Locators
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"
        self.view_cart_in_modal = "#cartModal a[href='/view_cart']"
        self.cart_modal = "#cartModal"
        self.cart_page_identifier = ".cart_info"

    def navigate(self):
        self.logger.info("Navigating to shop page")
        self.page.goto(Settings.SHOP_URL)  # works once SHOP_URL is defined
        self.page.wait_for_load_state("networkidle")

    def add_item_to_cart(self):
        self.logger.info("Adding item to cart")
        self.page.locator(self.add_to_cart_button).scroll_into_view_if_needed()

        try:
            self.click(self.add_to_cart_button)
        except Exception:
            self.logger.warning("Standard click failed, using JS click fallback")
            self.page.locator(self.add_to_cart_button).evaluate("el => el.click()")

        self.wait(self.cart_modal)
        self.click(self.view_cart_in_modal)
        self.page.wait_for_load_state("networkidle")

        if not self.is_cart_page():
            raise AssertionError(f"Not on cart page. URL: {self.page.url}")

    def is_cart_page(self) -> bool:
        return self.page.url.endswith("/view_cart") and \
            self.page.is_visible("table.cart_info")

