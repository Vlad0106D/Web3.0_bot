import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    setup_handlers(app)

    # 💥 Удаляем вебхук перед polling, иначе Telegram даст Conflict
    await app.bot.delete_webhook(drop_pending_updates=True)

    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())