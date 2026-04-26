import asyncio
import os
import threading
from flask import Flask
from telethon import TelegramClient

# መረጃዎችህን እዚህ አስገባ
API_ID = 39649767
API_HASH = "662122151abb4c6287102dbde7398484"
BOT_TOKEN = "8729663961:AAFMVyWOH4Kn8oBImfauFjuwtaHFOHfETus"
CHANNEL = "@KwasAfkari"

# Flask ለ Railway መቆያ (Health Check)
app = Flask('')
@app.route('/')
def home(): return "✅ KwasAfkari Bot is alive."

def run_flask():
    # Railway በራሱ PORT ይሰጠናል
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

async def start_bot():
    # ቦቱን ማስነሳት
    client = TelegramClient('bot_session', API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    print("ቦቱ ስራ ጀምሯል!")
    
    while True:
        # ለሙከራ ያህል በየ 10 ደቂቃው መልዕክት ይልካል
        await client.send_message(CHANNEL, "⚽ ኳስ አፍቃሪ ቦት በ Railway ላይ ስራ ጀምሯል።")
        await asyncio.sleep(600)

if __name__ == "__main__":
    # Flask እና Bot በአንድ ላይ እንዲሰሩ
    threading.Thread(target=run_flask).start()
    asyncio.run(start_bot())

