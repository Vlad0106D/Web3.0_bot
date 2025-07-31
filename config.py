import os

# Telegram bot token (из переменных окружения)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Активные пары для анализа
TRADING_PAIRS = [
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "SUIUSDT",
    "APTUSDT", "ARBUSDT", "OPUSDT", "STXUSDT", "TIAUSDT"
]

# Общие параметры стратегии
TIMEFRAMES = {
    "trend": "1d",     # таймфрейм для фильтрации тренда
    "signal": "1h",    # основной таймфрейм для входа
    "confirm": "4h"    # таймфрейм для подтверждения сигнала
}