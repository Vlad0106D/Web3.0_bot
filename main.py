import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

from quart import Quart

# Инициализируем Quart
app_web = Quart(__name__)

@app_web.route('/')
async def index():
    return "Web3 Bot is running"

async def start_bot():
    bot_app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(bot_app)
    print("Telegram bot is running...")
    await bot_app.run_polling()

async def start_web():
    print("Web server is running...")
    await app_web.run_task(host="0.0.0.0", port=8080)

async def main():
    await asyncio.gather(
        start_bot(),
        start_web()
    )

if __name__ == "__main__":
    asyncio.run(main())