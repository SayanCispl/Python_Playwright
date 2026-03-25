# Playwright Pytest Automation for automationexercise.com

**What this repo contains**

- Playwright tests written in Python using **pytest**.
- **Allure** reporting integration.
- Page Object Model under `pages/`.
- Example tests under `tests/` for **registration**, **login**, and **add-to-cart**.
- Dockerfile to run tests in a container.
- GitHub Actions workflow to run tests and upload Allure results.
- `.env` support for base URL and credentials.

---

## Project layout

project/
├─ pages/
│  ├─ base_page.py
│  ├─ home_page.py
│  ├─ login_page.py
│  ├─ register_page.py
│  └─ product_page.py
├─ tests/
│  ├─ test_registration.py
│  ├─ test_login.py
│  └─ test_add_to_cart.py
├─ .github/workflows/ci.yml
├─ .env
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
├─ Dockerfile
├─ .gitignore
└─ .dockerignore


---

## Prerequisites

- **Python 3.11+**
- **pip**
- **Playwright CLI** (installed via pip package)
- **Allure commandline** if you want to view reports locally

---

## Quick start locally

1. **Clone repo**
```bash
git clone <your-repo-url>
cd project

2. Create virtual environment and install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install

3. Run tests
pytest --alluredir=allure-results -q

4. Open Allure report locally
# requires allure commandline installed
allure serve allure-results

Docker
Build image
docker build -t playwright-tests:latest .

Run container
docker run --rm -e BASE_URL=https://automationexercise.com -e HEADLESS=true playwright-tests:latest

Allure results will be inside the container at allure-results. Mount a volume to persist results if needed.

GitHub Actions CI
Workflow file is .github/workflows/ci.yml.

Add repository Secrets TEST_USER_EMAIL and TEST_USER_PASSWORD if you want the login test to use an existing account.

The workflow runs tests and uploads allure-results as an artifact.

Environment variables
BASE_URL: Base URL of the site under test.

TEST_USER_EMAIL: Email for login test.

TEST_USER_PASSWORD: Password for login test.

HEADLESS: true or false to control headless mode.

Store these in .env locally and in GitHub Secrets for CI.

Useful commands
Run tests: pytest -q

Run single test: pytest tests/test_login.py::test_login -q

Generate Allure HTML: allure generate allure-results -o allure-report --clean

Serve Allure: allure serve allure-results

Notes and tips
Selectors in the example POM are illustrative. Inspect the live site and update selectors for stability.

Use timestamped emails in registration tests to avoid collisions.

Use HEADLESS=false locally for debugging.

Add retries or Playwright tracing for flaky tests.

Files to review and customize
conftest.py for fixtures and environment loading.

pages/* for POM selectors and helper methods.

tests/* for example flows.

Dockerfile for containerized runs.

.github/workflows/ci.yml for CI behavior.


