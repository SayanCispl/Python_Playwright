import allure
from pages.login_page import LoginPage

@allure.feature("Authentication")
@allure.story("Valid login")
@allure.severity(allure.severity_level.BLOCKER)
def test_login(page):
    login = LoginPage(page, test_name="test_login")  # ✅ no extra kwargs

    with allure.step("Navigate to login page"):
        login.open()

    with allure.step("Enter credentials and submit"):
        login.login()

    with allure.step("Validate successful login"):
        assert login.is_logged_in(), "Login failed"

    allure.attach(
        page.screenshot(),
        name="Post Login",
        attachment_type=allure.attachment_type.PNG
    )