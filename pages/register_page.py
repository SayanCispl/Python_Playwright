from pages.base_page import BasePage
import time

class RegisterPage(BasePage):
    def start_registration(self, name: str, email: str):
        # On the login page, there's a signup form on the right side
        # Fill in the name and email fields
        try:
            self.page.fill("input[data-qa='signup-name']", name)
        except Exception as e:
            print(f"Error filling signup name: {e}")
            # Try alternative selector
            self.page.fill("input[name='name']", name)

        try:
            self.page.fill("input[data-qa='signup-email']", email)
        except Exception as e:
            print(f"Error filling signup email: {e}")
            # Try alternative selector
            self.page.fill("input[name='email']", email)

        try:
            self.page.click("button[data-qa='signup-button']")
        except Exception as e:
            print(f"Error clicking signup button: {e}")
            self.page.click("button:has-text('Signup')")

        # Wait for the form to load
        self.page.wait_for_load_state("networkidle")
        time.sleep(1)

    def fill_account_details(self, password: str):
        # Wait for the account creation form to be visible
        try:
            self.page.wait_for_selector("input[id='password']", timeout=10000)
        except:
            print("Password field not found, trying alternative selectors")
            try:
                self.page.wait_for_selector("input[name='password']", timeout=5000)
            except:
                print("No password field found at all")
                return

        time.sleep(1)  # Give the form time to stabilize

        # Fill in password
        try:
            self.page.fill("input[id='password']", password)
        except:
            self.page.fill("input[name='password']", password)

        # Try to fill optional fields if they exist
        try:
            # Select title - try to check Mr. radio button
            self.page.check("input[id='id_gender1']")
        except:
            pass

        try:
            # Select day
            self.page.select_option("select[id='days']", "1")
        except:
            pass

        try:
            # Select month
            self.page.select_option("select[id='months']", "1")
        except:
            pass

        try:
            # Select year
            self.page.select_option("select[id='years']", "1990")
        except:
            pass

        # Scroll to create account button to ensure it's visible
        try:
            self.page.click("button[data-qa='create-account']")
        except:
            try:
                self.page.click("button:has-text('Create Account')")
            except:
                self.page.click("button[type='submit']")

        # Wait for success page
        self.page.wait_for_load_state("networkidle")
        time.sleep(2)


