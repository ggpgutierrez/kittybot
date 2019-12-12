import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HTTPS_CATS_URL = os.getenv("BASE_HTTP_URL")