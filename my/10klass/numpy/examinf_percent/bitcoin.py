import requests
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7"
response = requests.get(url)
data = response.json()
prices = data["prices"]  # список в формате [[timestamp, price], ...]
dates = [datetime.fromtimestamp(timestamp // 1000).strftime('%d.%m') for timestamp, _ in prices]
values = [price for _, price in prices]
plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker='o', linestyle='-', color='b')
plt.title("Курс биткоина за последние 7 дней (USD)")
plt.xlabel("Дата")
plt.ylabel("Цена (USD)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()