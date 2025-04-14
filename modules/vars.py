import os

API_ID    = os.environ.get("23171328", "")
API_HASH  = os.environ.get("6ddc5297d7944557b225b54968efe0b8", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8899))  # Default to 8000 if not set
