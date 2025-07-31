import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(app)

    # Удаляем старый webhook, если был
    await app.bot.delete_webhook(drop_pending_updates=True)

    print("Бот запущен...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # run_polling НЕ используем — он ломает loop в Python 3.13

if __name__ == "__main__":
    asyncio.run(main())