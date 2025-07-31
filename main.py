import os
import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Удаляем webhook, чтобы бот работал через polling
    await application.bot.delete_webhook(drop_pending_updates=True)

    # Подключаем команды
    setup_handlers(application)

    print("✅ Бот запущен через polling...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())