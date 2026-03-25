import pytest
import allure
from pages.login_page import LoginPage
from config.settings import Settings

@allure.feature("Authentication")
@allure.story("Valid login")
@allure.severity(allure.severity_level.BLOCKER)
def test_login(page):
    login = LoginPage(
        page,
        test_name="test_login",
        base_url=Settings.BASE_URL,
        username=Settings.USERNAME,
        password=Settings.PASSWORD
    )

    with allure.step("Navigate to login page"):
        login.open()

    with allure.step("Enter credentials and submit"):
        login.login()

    with allure.step("Validate successful login"):
        assert login.is_logged_in(), "Login failed"

    # Optional: attach screenshot after success
    allure.attach(
        page.screenshot(),
        name="Post Login",
        attachment_type=allure.attachment_type.PNG
    )
