
import os
import time
import requests
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8041021589:AAFuD-HElQI4yehKOJ328-V50XFhk9XQWfQ")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "2066686801")
API_KEY = os.getenv("TWELVE_DATA_API_KEY", "demo_key_123456")

SYMBOLS = ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/CHF", "NZD/USD", "USD/CAD", "EUR/GBP", "CAD/CHF"]

def fetch_price(symbol):
    url = f"https://api.twelvedata.com/price?symbol={symbol.replace('/', '')}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        return float(response.json().get("price", 0))
    except Exception as e:
        return 0

def send_signal(symbol, price, otc=False):
    status = "OTC" if otc else "REAL"
    message = f"🔔 {symbol} ({status})\nCurrent Price: {price}\nSignal: BUY or SELL (Based on strategy)"
    Bot(token=TELEGRAM_TOKEN).send_message(chat_id=CHAT_ID, text=message)

def main():
    for symbol in SYMBOLS:
        price = fetch_price(symbol)
        if price > 0:
            otc = ".O" in symbol or "OTC" in symbol.upper()
            send_signal(symbol, price, otc=otc)
        time.sleep(1)

if __name__ == "__main__":
    main()
