from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Удаляем Webhook, если остался
    application.bot.delete_webhook(drop_pending_updates=True)

    # Подключаем команды
    setup_handlers(application)

    print("✅ Бот запущен через polling (финально, без asyncio.run)...")

    # Запускаем polling (синхронно, без asyncio.run)
    application.run_polling()

if __name__ == "__main__":
    main()