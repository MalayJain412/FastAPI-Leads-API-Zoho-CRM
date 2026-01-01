import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
    ZOHO_BASE_URL = os.getenv("ZOHO_BASE_URL")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    AUTH_URL = os.getenv("OAUTH_AUTH_URL")
    TOKEN_URL = os.getenv("OAUTH_TOKEN_URL")

settings = Settings()
