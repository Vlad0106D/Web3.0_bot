from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(app)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()