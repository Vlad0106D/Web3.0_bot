import aiohttp

BASE_URL = "https://api.coingecko.com/api/v3"

# Сопоставление тикеров с CoinGecko ID
SYMBOL_TO_ID = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "XRP": "ripple",
    "SUI": "suichain",
    "APT": "aptos",
    "ARB": "arbitrum",
    "OP": "optimism",
    "STX": "stacks",
    "TIA": "celestia",
    "INJ": "injective-protocol",
    "XLM": "stellar",
    "ACH": "alchemy-pay",
    "COTI": "coti",
    "FET": "fetch-ai",
    "TAO": "bittensor",
    "RNDR": "render-token",
    "LINK": "chainlink",
    "GLMR": "moonbeam",
    "ANKR": "ankr",
    "ONDO": "ondo-finance",
    "POLYX": "polyx"
}

async def get_market_data(pair: str):
    """
    Получает рыночные данные по тикеру, например: "BTC", "ETH", "SOL"
    Возвращает: словарь с ценой, объемом, изменением и капитализацией.
    """
    try:
        coin_id = SYMBOL_TO_ID.get(pair.upper())
        if not coin_id:
            print(f"[get_market_data] Неизвестный тикер: {pair}")
            return {}

        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": "usd",
            "ids": coin_id
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()
                if not data:
                    return {}

                coin = data[0]
                return {
                    "price": coin.get("current_price"),
                    "volume_24h": coin.get("total_volume"),
                    "change_24h": coin.get("price_change_percentage_24h"),
                    "market_cap": coin.get("market_cap")
                }

    except Exception as e:
        print(f"[get_market_data] Ошибка: {e}")
        return {}