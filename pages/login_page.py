from pages.base_page import BasePage
from config.settings import Settings

class LoginPage(BasePage):
    def __init__(self, page, test_name="login_test"):
        super().__init__(page, test_name)
        self.base_url = Settings.BASE_URL
        self.username = Settings.USERNAME
        self.password = Settings.PASSWORD

    def open(self):
        self.page.goto(f"{self.base_url}/login")

    def login(self):
        self.page.fill("input[data-qa='login-email']", self.username)
        self.page.fill("input[data-qa='login-password']", self.password)
        self.page.click("button[data-qa='login-button']")

    def is_logged_in(self):
        return self.page.is_visible("text=Logout")
