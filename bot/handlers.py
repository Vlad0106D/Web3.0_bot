from telegram import Update
from telegram.ext import ContextTypes
from base_strategy import analyze_market  # ✅ правильный импорт

# Список 10 активных пар
PAIRS = [
    "BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "SUI/USDT",
    "APT/USDT", "ARB/USDT", "OP/USDT", "STX/USDT", "TIA/USDT"
]

# Команда /check
async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Анализ рынка... Подождите 10–15 сек.")
    results = analyze_market(PAIRS)
    
    for res in results:
        text = f"🔹 *{res['symbol']}*\nСигнал: *{res['signal']}*"
        if res['reasons']:
            text += "\nПричины:\n" + "\n".join(f"- {r}" for r in res['reasons'])
        await update.message.reply_text(text, parse_mode="Markdown")