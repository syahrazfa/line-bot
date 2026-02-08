from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv
import os

load_dotenv()

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))

users = [
    "raz.fa"
]

for user_id in users:
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text="Hai ganteng")
    )
