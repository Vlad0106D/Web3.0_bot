# bot/handlers.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application
from strategy.base_strategy import analyze_market  # ✅ исправили импорт

PAIRS = [
    "BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "SUI/USDT",
    "APT/USDT", "ARB/USDT", "OP/USDT", "STX/USDT", "TIA/USDT"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Бот работает. Используй /check для анализа рынка.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Команды:\n/start — запуск бота\n/help — помощь\n/check — анализ рынка")

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Анализ рынка... Пожалуйста, подождите ⏳")
    try:
        report = await analyze_market(PAIRS)
        await update.message.reply_text(report)
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка анализа: {e}")

def setup_handlers(application: Application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("check", check_command))