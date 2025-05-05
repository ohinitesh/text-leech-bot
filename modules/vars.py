import os

API_ID    = os.environ.get("API_ID", "23171328")
API_HASH  = os.environ.get("API_HASH", "6ddc5297d7944557b225b54968efe0b8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8030725454:AAFdRHpOAXKxwW-RaY9-cx0uJzhT3bQrvo8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8899))  # Default to 8000 if not set
