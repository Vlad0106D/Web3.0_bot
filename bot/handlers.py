from telegram.ext import CommandHandler, Application

async def start(update, context):
    await update.message.reply_text("👋 Бот работает. Используй /check для анализа рынка.")

async def help_command(update, context):
    await update.message.reply_text("Доступные команды:\n/start — запуск\n/check — анализ")

def setup_handlers(application: Application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))