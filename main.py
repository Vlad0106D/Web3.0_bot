import asyncio
from telegram.ext import ApplicationBuilder
from config import TOKEN
from bot.handlers import setup_handlers

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(application)
    print("✅ Бот запущен через polling...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) != 'Cannot close a running event loop':
            raise