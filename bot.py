
import os
import time
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alert(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram variables are missing")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

    print("Telegram response:", response.text)

print("Meme Coin Alert Bot is ONLINE!")
send_alert("🚀 Meme Coin Alert Bot is ONLINE!")

while True:
    print("Bot running...")
    time.sleep(60)
