from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Подключаем обработчики
    setup_handlers(application)

    print("✅ Бот запущен через polling...")

    # Синхронный запуск без async (не использовать asyncio.run)
    application.run_polling()
    
if __name__ == "__main__":
    main()