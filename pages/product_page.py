from config.settings import Settings
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page, test_name="product_test"):
        super().__init__(page, test_name)

        # Correct locators
        self.search_box = "#search_product"
        self.search_button = "button[id='submit_search']"  # safer than generic type=submit
        self.searched_products_header = "h2:has-text('Searched Products')"
        self.blue_top_add_to_cart = "(//a[contains(text(),'Add to cart')])[1]"
        self.cart_modal = "#cartModal"
        self.view_cart_in_modal = "#cartModal a[href='/view_cart']"

    def search_product(self, name: str):
        self.logger.info(f"Searching for product: {name}")

        # Navigate to the Products page (not just BASE_URL)
        self.page.goto(f"{Settings.BASE_URL}/products")
        self.page.wait_for_load_state("networkidle")

        # Fill search box and submit
        self.page.fill("#search_product", name)
        self.page.click("#submit_search")

        # Wait for results header
        self.wait("h2:has-text('Searched Products')")

    def add_blue_top_to_cart(self):
        """Click 'Add to Cart' for Blue Top and go to cart."""
        self.logger.info("Adding Blue Top to cart")

        self.page.locator(self.blue_top_add_to_cart).scroll_into_view_if_needed()
        try:
            self.click(self.blue_top_add_to_cart)
        except Exception:
            self.logger.warning("Standard click failed, using JS click fallback")
            self.page.locator(self.blue_top_add_to_cart).evaluate("el => el.click()")

        self.wait(self.cart_modal)
        self.click(self.view_cart_in_modal)
        self.page.wait_for_load_state("networkidle")
