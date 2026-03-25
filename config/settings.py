import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL")
    SHOP_URL = os.getenv("SHOP_URL", f"{BASE_URL}/products")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")