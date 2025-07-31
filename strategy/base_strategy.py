from services.coingecko import get_market_data

async def analyze_pair(symbol: str):
    price = await get_market_data(symbol)
    if price is None:
        return f"{symbol.upper()}: нет данных"

    # Здесь будет стратегия. Пока просто сигнал:
    signal = "🔼 LONG" if price and price > 1000 else "🔽 SHORT"
    return f"{symbol.upper()}: ${price} — {signal}"