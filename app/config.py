import os
from dotenv import load_dotenv

load_dotenv()  # Tải biến môi trường từ file .env

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
MODEL = os.getenv("MODEL")
