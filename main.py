import os
import sys
import subprocess
from dotenv import load_dotenv

# Ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def main():
    # Load environment variables from .env
    load_dotenv()

    base_url = os.getenv("BASE_URL", "https://automationexercise.com")
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    print(f"Running tests against {base_url} (headless={headless})")

    # Build pytest command
    cmd = [
        "pytest",
        "--browser", "chromium",
        "--base-url", base_url,
        "--alluredir=allure-results",
        "-q"
    ]

    # Playwright pytest plugin does not support --headless flag.
    # Use PWDEBUG=1 to force headed mode if HEADLESS=false
    if not headless:
        os.environ["PWDEBUG"] = "1"

    # Allow passing extra args to pytest
    if len(sys.argv) > 1:
        cmd.extend(sys.argv[1:])

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
