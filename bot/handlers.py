from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# Импорт существующих команд
from bot.commands.check import check_command

# Команда /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я Web3 трейдинг-бот.\n\n"
        "Доступные команды:\n"
        "/check — технический анализ и сигналы\n"
        "/help — справка"
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Помощь:\n"
        "/check — запустить анализ рынка\n"
        "/start — приветствие и описание\n"
        "/help — эта справка"
    )

# Регистрация всех команд
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("check", check_command))