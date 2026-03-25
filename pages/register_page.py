from config.settings import Settings

class RegistrationPage:
    def __init__(self, page):
        self.page = page

    def register(self, name, email):
        # Navigate to the site first
        self.page.goto(Settings.BASE_URL)

        # Click the Signup / Login link in the header
        self.page.click("text=Signup / Login")

        # Fill in the signup form fields
        self.page.fill("input[data-qa='signup-name']", name)
        self.page.fill("input[data-qa='signup-email']", email)

        # Click the Signup button
        self.page.click("button[data-qa='signup-button']")
