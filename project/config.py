import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# LINE Bot 設定
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
GOOGLE_API_KEY = os.environ.get('GEMINI_KEY')
FIREBASE_URL = os.environ.get('FIREBASE_URL')
