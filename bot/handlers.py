from telegram import Update
from telegram.ext import ContextTypes
from strategy.base_strategy import analyze_market  # ✅ правильный импорт
from telegram.ext import Application, CommandHandler

# 🔹 Список пар для анализа (топ-10)
PAIRS = [
    "BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "SUI/USDT",
    "APT/USDT", "ARB/USDT", "OP/USDT", "STX/USDT", "TIA/USDT"
]

# 🔍 Команда /check — анализ рынка
async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Анализ рынка... Пожалуйста, подождите ⏳")

    try:
        results = analyze_market(PAIRS)
        for res in results:
            text = f"🔹 *{res['symbol']}*\nСигнал: *{res['signal']}*"
            if res['reasons']:
                text += "\nПричины:\n" + "\n".join(f"- {r}" for r in res['reasons'])
            await update.message.reply_text(text, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка анализа: {str(e)}")

# ✅ Функция для main.py
def setup_handlers(application: Application):
    application.add_handler(CommandHandler("check", check_command))