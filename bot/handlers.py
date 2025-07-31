# bot/handlers.py

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from strategy.base_strategy import analyze_pair

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    results = await analyze_pair()
    message = "\n".join([f"{pair.upper()}: {signal}" for pair, signal in results.items()])
    await update.message.reply_text(f"📊 Сигналы по рынку:\n{message}")

def setup_handlers(app):
    app.add_handler(CommandHandler("check", check_command))