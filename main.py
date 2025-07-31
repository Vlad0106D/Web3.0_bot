import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Удаляем webhook перед запуском polling
    await app.bot.delete_webhook(drop_pending_updates=True)

    setup_handlers(app)

    print("✅ Бот запущен")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # Запускаем loop бесконечно, пока не остановим вручную
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        print(f"❌ RuntimeError: {e}")