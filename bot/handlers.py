from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Бот работает и готов к анализу!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Доступные команды:\n/start — запуск\n/help — помощь")

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))