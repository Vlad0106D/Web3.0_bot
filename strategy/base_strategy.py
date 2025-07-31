from pybit.unified_trading import HTTP
import pandas as pd
import ta

# Подключаемся к публичному API Bybit
session = HTTP()

def fetch_ohlcv(symbol, interval="60", limit=200):
    try:
        # symbol пример: BTC/USDT → BTCUSDT
        market = symbol.replace("/", "")
        res = session.get_kline(
            category="linear",
            symbol=market,
            interval=interval,  # "60" = 1h, "240" = 4h, "D" = 1d
            limit=limit
        )
        kline = res["result"]["list"]
        df = pd.DataFrame(kline, columns=[
            "timestamp", "open", "high", "low", "close", "volume", "turnover"
        ])
        df = df.sort_values(by="timestamp")
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
        return df
    except Exception as e:
        raise RuntimeError(f"Ошибка загрузки данных с Bybit: {e}")

def analyze_pair(symbol):
    try:
        df = fetch_ohlcv(symbol, interval="60", limit=200)

        df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
        macd = ta.trend.MACD(df["close"])
        df["macd"] = macd.macd()
        df["macd_signal"] = macd.macd_signal()
        df["adx"] = ta.trend.ADXIndicator(df["high"], df["low"], df["close"], window=14).adx()
        df["atr"] = ta.volatility.AverageTrueRange(df["high"], df["low"], df["close"]).average_true_range()

        last = df.iloc[-1]
        signal = "NONE"
        reasons = []

        if last["rsi"] < 35:
            reasons.append(f"RSI = {last['rsi']:.1f} (перепроданность)")
        if last["macd"] > last["macd_signal"]:
            reasons.append("MACD пересёк вверх")
        if last["adx"] > 20:
            reasons.append(f"ADX = {last['adx']:.1f} (тренд есть)")

        if len(reasons) >= 2:
            signal = "LONG ✅"
        elif last["rsi"] > 65 and last["macd"] < last["macd_signal"]:
            signal = "SHORT ⚠️"
            reasons = [f"RSI = {last['rsi']:.1f}", "MACD пересёк вниз"]

        return {
            "symbol": symbol,
            "signal": signal,
            "reasons": reasons
        }

    except Exception as e:
        return {
            "symbol": symbol,
            "signal": "ERROR",
            "reasons": [str(e)]
        }

def analyze_market(pairs):
    results = []
    btc_signal = analyze_pair("BTC/USDT")
    for pair in pairs:
        if pair == "BTC/USDT":
            results.append(btc_signal)
            continue
        res = analyze_pair(pair)
        if btc_signal["signal"] == "NONE":
            res["signal"] = "NONE"
            res["reasons"].insert(0, "BTC не даёт подтверждения")
        results.append(res)
    return results