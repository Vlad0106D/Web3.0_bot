# strategy/base_strategy.py

from services.coingecko import get_market_data
from config import PAIRS, VS_CURRENCY

async def analyze_pair():
    signals = {}
    for coin in PAIRS:
        data = await get_market_data(coin)
        if not data:
            signals[coin] = "нет данных"
            continue

        change = data.get("price_change_percentage_24h", 0)
        if change > 2:
            signals[coin] = "🔼 LONG"
        elif change < -2:
            signals[coin] = "🔽 SHORT"
        else:
            signals[coin] = "⏸️ NONE"
    return signals
