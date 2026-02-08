from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv
import os

load_dotenv()

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))

with open("./users.txt") as f:
    user_ids = [line.strip() for line in f if line.strip()]

for user_id in user_ids:
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text="Scheduled broadcast message")
    )