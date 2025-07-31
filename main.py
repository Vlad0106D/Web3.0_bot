# main.py

import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(app)
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())