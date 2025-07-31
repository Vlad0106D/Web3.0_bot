import aiohttp

BASE_URL = "https://api.coingecko.com/api/v3"

async def get_market_data(pair: str):
    """
    Получает рыночные данные по торговой паре, например: "bitcoin", "ethereum"
    Возвращает: {price, volume_24h, change_24h}
    """
    try:
        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": "usd",
            "ids": pair.lower()
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
        print(f"[get_market_data] Ошибка при запросе данных: {e}")
        return {}
