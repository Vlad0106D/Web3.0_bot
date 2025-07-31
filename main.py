import os
import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def run_bot():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(application)

    # Удаляем webhook перед стартом polling
    await application.bot.delete_webhook(drop_pending_updates=True)

    print("✅ Бот запущен через polling...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    asyncio.run(run_bot())