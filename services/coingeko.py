# services/coingecko.py

import httpx
from config import VS_CURRENCY

async def get_market_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": VS_CURRENCY,
        "ids": coin_id,
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            if response.status_code == 200 and response.json():
                return response.json()[0]
    except Exception as e:
        print(f"Ошибка при запросе данных CoinGecko: {e}")
    return None
