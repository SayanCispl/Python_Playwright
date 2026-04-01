from pages.base_page import BasePage
from config.settings import Settings

class LoginPage(BasePage):
    def __init__(self, page, test_name="login_test"):
        super().__init__(page, test_name)
        self.base_url = Settings.BASE_URL
        self.username = Settings.APP_USERNAME
        self.password = Settings.PASSWORD

    def open(self):
        self.page.goto(f"{self.base_url}/login")
        self.page.wait_for_load_state("networkidle")  # ✅ wait for full page load

    def login(self):
        self.page.fill("input[data-qa='login-email']", self.username)
        self.page.fill("input[data-qa='login-password']", self.password)
        self.page.click("button[data-qa='login-button']")
        self.page.wait_for_load_state("networkidle")  # ✅ wait for post-login navigation

    def is_logged_in(self):
        try:
            # ✅ wait up to 10s instead of instant snapshot with is_visible()
            self.page.wait_for_selector("a[href='/logout']", timeout=10000)
            return True
        except Exception:
            return False