import os
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# Удаляем вебхук (если он был) перед запуском polling
async def on_startup(app):
    await app.bot.delete_webhook(drop_pending_updates=True)

# Регистрируем команды
setup_handlers(application)

# ✅ Передаём startup callback
application.run_polling(on_startup=on_startup)