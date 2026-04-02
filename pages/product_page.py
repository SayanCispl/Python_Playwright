from pages.base_page import BasePage
from config.settings import Settings


class ProductPage(BasePage):
    def __init__(self, page, test_name="product_test"):
        super().__init__(page, test_name)

    def open_products(self):
        self.page.goto(f"{Settings.BASE_URL}/products")
        self.page.wait_for_load_state("networkidle")

    def search_product(self, product_name):
        self.open_products()
        self.page.wait_for_selector("#search_product", timeout=10000)
        self.page.fill("#search_product", product_name)
        self.page.click("#submit_search")
        self.page.wait_for_load_state("networkidle")

    def add_blue_top_to_cart(self):
        self.logger.info("Adding Blue Top to cart")

        # ✅ Import here to avoid circular imports
        from pages.cart_page import CartPage

        # ✅ Wait for products to load
        self.page.wait_for_selector(".product-image-wrapper", timeout=10000)

        # ✅ Hover and click Add to Cart on first product
        first_product = self.page.locator(".product-image-wrapper").first
        first_product.hover()
        first_product.locator("a.add-to-cart").click()

        # ✅ Handle modal and navigate to cart
        cart = CartPage(self.page, test_name="product_add_to_cart")
        cart.handle_cart_modal()

        if not cart.is_cart_page():
            raise AssertionError(
                f"Not on cart page after adding product. URL: {self.page.url}"
            )