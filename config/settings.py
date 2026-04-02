import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
    APP_USERNAME = os.getenv("APP_USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SHOP_URL = os.getenv("SHOP_URL") or f"{BASE_URL}/products" # ✅ works at class level

    @classmethod
    def shop_url(cls):
        return cls.SHOP_URL