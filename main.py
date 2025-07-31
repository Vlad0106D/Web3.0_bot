# main.py

import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_TOKEN

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    setup_handlers(application)
    print("✅ Бот запущен через polling...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())