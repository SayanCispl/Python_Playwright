import allure
from pages.register_page import RegistrationPage

@allure.feature("Authentication")
@allure.story("User Registration")
@allure.severity(allure.severity_level.CRITICAL)
def test_registration(page):
    reg = RegistrationPage(page)

    with allure.step("Register a new user"):
        reg.register("Test User", "testuser@example.com")

    allure.attach(
        page.screenshot(),
        name="Post Registration",
        attachment_type=allure.attachment_type.PNG
    )
