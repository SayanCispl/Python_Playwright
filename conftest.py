import os
import allure
import pytest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL", "")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD", "")

@pytest.fixture
def credentials():
    """Provide login credentials from .env file."""
    return {"email": TEST_USER_EMAIL, "password": TEST_USER_PASSWORD}

# Attach screenshot and page source on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            try:
                png = page.screenshot(full_page=True)
                allure.attach(png, name="screenshot", attachment_type=allure.attachment_type.PNG)
                html = page.content()
                allure.attach(html, name="page_source", attachment_type=allure.attachment_type.HTML)
            except Exception:
                pass
