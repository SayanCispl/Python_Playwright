from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email: str, password: str):
        """Log in with email and password."""
        # Try multiple selector patterns for login form
        email_input = None
        password_input = None
        login_button = None

        # Try to find email input
        try:
            self.page.fill("input[data-qa='login-email']", email)
            email_input = True
        except:
            try:
                self.page.fill("input[placeholder='Email Address']", email)
                email_input = True
            except:
                try:
                    self.page.fill("input[name='email']", email)
                    email_input = True
                except:
                    pass

        # Try to find password input
        try:
            self.page.fill("input[data-qa='login-password']", password)
            password_input = True
        except:
            try:
                self.page.fill("input[placeholder='Password']", password)
                password_input = True
            except:
                try:
                    self.page.fill("input[name='password']", password)
                    password_input = True
                except:
                    pass

        # Try to find login button
        try:
            self.page.click("button[data-qa='login-button']")
            login_button = True
        except:
            try:
                self.page.click("button:has-text('Login')")
                login_button = True
            except:
                try:
                    self.page.click("button[type='submit']")
                    login_button = True
                except:
                    pass

        # Wait for navigation to complete
        self.page.wait_for_load_state("networkidle")

    def is_logged_in(self) -> bool:
        """Check if user is logged in by looking for logout button."""
        # On automationexercise, logged-in users see a logout link
        return self.page.locator("a[href='/logout']").is_visible()

