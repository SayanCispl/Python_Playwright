# Product Page (Search + Add to Cart)

class ProductPage:
    def __init__(self, page):
        self.page = page

    def open_products(self):
        self.page.click("text=Products")

    def search_product(self, product_name):
        self.page.fill("#search_product", product_name)
        self.page.click("#submit_search")

    def add_to_cart(self):
        self.page.hover(".product-image-wrapper")
        self.page.click("text=Add to cart")

    def view_cart(self):
        self.page.click("text=View Cart")