from pages.base_page import BasePage

class ProductPage(BasePage):
    def add_first_product_to_cart(self):
        # On automationexercise, products are listed; click first 'Add to cart'
        # Use a robust selector for the first product's add-to-cart button
        try:
            self.page.locator("a.add-to-cart").first.click()
        except:
            try:
                # Try alternative selector
                self.page.click("button[data-product-id]:has-text('Add to cart')")
            except:
                try:
                    # Try another variation
                    self.page.click("a:has-text('Add to cart')")
                except:
                    pass

        # Wait for modal and continue shopping or view cart
        try:
            self.page.wait_for_selector("#cartModal", timeout=5000)
            # Close modal if present
            if self.page.locator("button.close-modal").is_visible():
                self.page.click("button.close-modal")
        except:
            # Modal might not appear, continue
            pass
