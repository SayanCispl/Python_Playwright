from pages.base_page import BasePage

class HomePage(BasePage):
    def go_to_signup_login(self):
        self.page.click("a[href='/login']")

    def search_product(self, name: str):
        self.page.fill("input[name='search']", name)
        self.page.click("button[type='submit']")
