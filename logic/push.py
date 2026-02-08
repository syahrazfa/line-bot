import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_FILE = os.path.join(BASE_DIR, "users.txt")

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))

with open(USERS_FILE) as f:
    user_ids = [line.strip() for line in f if line.strip()]

for user_id in user_ids:
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text="hi tamvan")
    )

print("Push complete.")
