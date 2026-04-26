import asyncio
import os
import threading
from flask import Flask
from telethon import TelegramClient

# መረጃዎችህ
API_ID = 39649767
API_HASH = "662122151abb4c6287102dbde7398484"
BOT_TOKEN = "8729663961:AAFMVyWOH4Kn8oBImfauFjuwtaHFOHfETus"
CHANNEL = "@KwasAfkari"

app = Flask('')
@app.route('/')
def home(): return "✅ KwasAfkari Bot is alive."

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

async def start_bot():
    client = TelegramClient('bot_session', API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    print("✅ ቦቱ በስኬት ተነስቷል!")
    
    # ለሙከራ ያህል ወዲያውኑ መልእክት ይልካል
    await client.send_message(CHANNEL, "⚽ ኳስ አፍቃሪ ቦት በ Railway ላይ በስኬት ተነስተው ስራ ጀምሯል!")
    
    while True:
        await asyncio.sleep(600)

def run_bot_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())

if __name__ == "__main__":
    # Flaskን ለብቻው ማስነሳት
    threading.Thread(target=run_flask).start()
    # ቦቱን ለብቻው ማስነሳት
    run_bot_loop()
