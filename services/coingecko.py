import aiohttp

COINGECKO_IDS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    # добавь нужные тикеры
}

async def get_market_data(symbol: str):
    coingecko_id = COINGECKO_IDS.get(symbol.upper())
    if not coingecko_id:
        return None

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coingecko_id}&vs_currencies=usd"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data.get(coingecko_id, {}).get("usd")