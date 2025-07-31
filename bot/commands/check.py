from telegram import Update
from telegram.ext import ContextTypes
from strategy.base_strategy import analyze_pair

TARGET_PAIRS = ["BTC", "ETH"]  # потом заменим на твой список

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Анализ рынка запущен...")

    results = []
    for symbol in TARGET_PAIRS:
        result = await analyze_pair(symbol)
        results.append(result)

    message = "\n".join(results)
    await update.message.reply_text(message)