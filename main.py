import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

def main():
    # Создаём event loop вручную для Python 3.13
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(app)

    # Удаляем старый webhook (если был)
    loop.run_until_complete(app.bot.delete_webhook(drop_pending_updates=True))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()