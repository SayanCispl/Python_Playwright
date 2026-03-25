from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page, test_name, base_url, username, password):
        super().__init__(page, base_url)
        self.test_name = test_name
        self.username = username
        self.password = password

    def open(self):
        # Navigate directly to the login page
        self.page.goto(f"{self.base_url}/login")

    def login(self):
        # Fill in credentials
        self.page.fill("input[data-qa='login-email']", self.username)
        self.page.fill("input[data-qa='login-password']", self.password)
        self.page.click("button[data-qa='login-button']")

    def is_logged_in(self):
        # Check for a logout button or user profile element
        return self.page.is_visible("text=Logout")
