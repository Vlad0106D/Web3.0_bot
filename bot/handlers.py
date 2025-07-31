from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from bot.commands.check import check_command  # этот файл должен быть

# Команда /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Я Web3 трейдинг-бот.")

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Команды: /start, /check, /help")

# Регистрируем команды
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("check", check_command))