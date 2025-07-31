from telegram import Update
from telegram.ext import ContextTypes

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Анализ рынка запущен... (заглушка)")