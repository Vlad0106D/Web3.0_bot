import asyncio
from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
from config import TELEGRAM_BOT_TOKEN

from quart import Quart

# Quart-приложение
app_web = Quart(__name__)

@app_web.route('/')
async def index():
    return "Web3 Bot is running"

# Создаём Telegram-бота один раз
bot_app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
setup_handlers(bot_app)

async def start_bot():
    print("Запуск Telegram-бота...")
    await bot_app.initialize()
    await bot_app.start()
    await bot_app.updater.start_polling()
    # Не вызываем run_polling() — он завершает event loop

async def start_web():
    print("Запуск веб-сервера...")
    await app_web.run_task(host="0.0.0.0", port=8080)

async def main():
    await asyncio.gather(
        start_bot(),
        start_web()
    )

if __name__ == "__main__":
    asyncio.run(main())