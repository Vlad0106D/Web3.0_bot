import ccxt
import pandas as pd
import ta
from datetime import datetime, timedelta

exchange = ccxt.binance()

def fetch_ohlcv(symbol, timeframe='1h', limit=100):
    market = symbol.replace('/', '')
    data = exchange.fetch_ohlcv(market, timeframe, limit=limit)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def analyze_pair(symbol):
    try:
        df_4h = fetch_ohlcv(symbol, '4h', 100)
        df_1h = fetch_ohlcv(symbol, '1h', 100)
        
        df = df_1h.copy()
        df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
        df['macd'] = ta.trend.MACD(df['close']).macd()
        df['macd_signal'] = ta.trend.MACD(df['close']).macd_signal()
        df['adx'] = ta.trend.ADXIndicator(df['high'], df['low'], df['close'], window=14).adx()
        df['atr'] = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close']).average_true_range()
        
        last = df.iloc[-1]
        signal = "NONE"
        reasons = []

        if last['rsi'] < 35:
            reasons.append(f"RSI = {last['rsi']:.1f} (перепроданность)")
        if last['macd'] > last['macd_signal']:
            reasons.append("MACD пересёк вверх")
        if last['adx'] > 20:
            reasons.append(f"ADX = {last['adx']:.1f} (тренд есть)")
        
        if len(reasons) >= 2:
            signal = "LONG ✅"
        elif last['rsi'] > 65 and last['macd'] < last['macd_signal']:
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
        if btc_signal['signal'] == "NONE":
            res['signal'] = "NONE"
            res['reasons'].insert(0, "BTC не даёт подтверждения")
        results.append(res)
    return results