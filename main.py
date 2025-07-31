import os
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers

# Получаем токен из переменной окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    application.bot.delete_webhook(drop_pending_updates=True)

    setup_handlers(application)

    print("✅ Бот запущен через polling...")
    application.run_polling()

if __name__ == "__main__":
    main()