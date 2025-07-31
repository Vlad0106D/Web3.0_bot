import aiohttp
from config import VS_CURRENCY

async def get_market_data(coin_id):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": VS_CURRENCY,
        "ids": coin_id,
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data:
                        return data[0]
    except Exception as e:
        print(f"Ошибка при запросе CoinGecko: {e}")
    return None