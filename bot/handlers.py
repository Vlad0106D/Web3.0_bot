# bot/handlers.py

from telegram.ext import CommandHandler, Application
from telegram import Update
from telegram.ext import ContextTypes
from strategy.advanced_strategy import analyze_market  # Импорт стратегии

# Список криптопар для анализа
PAIRS = [
    "BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "SUI/USDT",
    "APT/USDT", "ARB/USDT", "OP/USDT", "STX/USDT", "TIA/USDT"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Бот работает. Используй /check для анализа рынка.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Доступные команды:\n/start — запуск\n/help — помощь\n/check — анализ рынка")

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Анализ рынка... Пожалуйста, подождите ⏳")

    try:
        results = analyze_market(PAIRS)
        if not results:
            await update.message.reply_text("❌ Сигналы не найдены.")
            return

        for res in results:
            text = f"🔹 *{res['symbol']}*\nСигнал: *{res['signal']}*"
            if res['reasons']:
                text += "\nПричины:\n" + "\n".join(f"- {r}" for r in res['reasons'])
            await update.message.reply_text(text, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка анализа: {str(e)}")

def setup_handlers(application: Application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("check", check_command))