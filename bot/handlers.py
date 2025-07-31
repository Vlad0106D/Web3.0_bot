from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from strategy.base_strategy import analyze_market

PAIRS = [
    "BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "SUI/USDT",
    "APT/USDT", "ARB/USDT", "OP/USDT", "STX/USDT", "TIA/USDT"
]

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Анализ рынка... Подождите ⏳")
    try:
        results = analyze_market(PAIRS)
        for res in results:
            text = f"🔹 *{res['symbol']}*\nСигнал: *{res['signal']}*"
            if res['reasons']:
                text += "\nПричины:\n" + "\n".join(f"- {r}" for r in res['reasons'])
            await update.message.reply_text(text, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка анализа: {str(e)}")

def setup_handlers(application: Application):
    application.add_handler(CommandHandler("check", check_command))