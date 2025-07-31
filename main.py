import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

async def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Удаляем Webhook, если остался
    await application.bot.delete_webhook(drop_pending_updates=True)

    # Подключаем команды
    setup_handlers(application)

    print("✅ Бот запущен через polling (без конфликтов)...")

    # Запускаем polling напрямую (без Updater, только Application)
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())