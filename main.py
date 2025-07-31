# main.py

from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TOKEN

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(application)
    print("✅ Бот запущен через polling...")
    application.run_polling()

if __name__ == "__main__":
    main()