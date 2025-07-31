import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем токен из переменной окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Остальная конфигурация
PAIRS = ["bitcoin", "ethereum"]
VS_CURRENCY = "usd"