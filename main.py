import os
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Создаём приложение
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# Регистрируем команды
setup_handlers(application)

# Запуск polling с удалением webhook
async def on_startup(app):
    await app.bot.delete_webhook(drop_pending_updates=True)
    print("✅ Бот запущен через polling...")

# Запускаем приложение
application.run_polling(on_startup=on_startup)