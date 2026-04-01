from pages.base_page import BasePage
from config.settings import Settings


class ProductPage(BasePage):
    def __init__(self, page, test_name="product_test"):
        super().__init__(page, test_name)

    def open_products(self):
        self.page.goto(f"{Settings.BASE_URL}/products")
        self.page.wait_for_load_state("networkidle")

    def search_product(self, product_name):
        self.open_products()  # ✅ navigate first before searching
        self.page.fill("#search_product", product_name)
        self.page.click("#submit_search")
        self.page.wait_for_load_state("networkidle")

    def add_to_cart(self):
        self.page.hover(".product-image-wrapper")
        self.page.click("text=Add to cart")
        self.page.wait_for_load_state("networkidle")

    def add_blue_top_to_cart(self):
        self.logger.info("Adding Blue Top to cart")
        # Wait for product list
        self.page.wait_for_selector(".product-image-wrapper", timeout=10000)

        # Hover and click Add to cart for the first product (Blue Top)
        self.page.hover(".product-image-wrapper:first-child")
        self.page.click(".product-image-wrapper:first-child .add-to-cart")

        # Wait for modal popup
        self.page.wait_for_selector("text=Your product has been added to cart.", timeout=5000)

        # Click "View Cart" link inside modal
        self.page.click("a[href='/view_cart']")

        # Wait for cart page to load
        self.page.wait_for_load_state("networkidle")

    def view_cart(self):
        self.page.click("text=View Cart")
        self.page.wait_for_load_state("networkidle")