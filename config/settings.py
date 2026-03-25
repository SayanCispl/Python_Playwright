import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL")
    SHOP_URL = os.getenv("SHOP_URL", f"{BASE_URL}/products")
    APP_USERNAME = os.getenv("APP_USERNAME")   # ✅ avoids system USERNAME clash
    PASSWORD = os.getenv("PASSWORD")
    test_name = "checkout_flow"