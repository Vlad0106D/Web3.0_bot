# main.py

import os
import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    setup_handlers(application)
    print("✅ Бот запущен через polling...")
    await application.run_polling()

# Проверка на уже запущенный event loop
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "already running" in str(e):
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()
        else:
            raise