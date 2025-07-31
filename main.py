# main.py

from telegram.ext import Application
from config import TOKEN
from bot.handlers import setup_handlers

def main():
    application = Application.builder().token(TOKEN).build()
    setup_handlers(application)
    print("✅ Бот запущен через polling...")
    application.run_polling()

if __name__ == "__main__":
    main()