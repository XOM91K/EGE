import requests
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Настройки API (замените 'ваш_api_ключ' на реальный ключ)
API_KEY = '80859c968f5e35887f0055bb206183eb'
CITY = 'Tokyo'

# 2. Получаем прогноз на 5 дней (каждые 3 часа)
url = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()

# 3. Извлекаем данные о температуре и времени
times = []
temps = []

for forecast in data['list'][:8]:  # Берем первые 8 точек (ближайшие 24 часа)
    time_str = forecast['dt_txt']
    temp = forecast['main']['temp']

    # Преобразуем время в удобный формат
    time_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    times.append(time_obj.strftime('%H:%M'))
    temps.append(temp)

    print(f"{time_obj.strftime('%H:%M')}: {temp}°C")

# 4. Строим график
plt.figure(figsize=(10, 5))
plt.plot(times, temps, marker='x', color='crimson', linewidth=2)
plt.title(f'Прогноз температуры в {CITY} на 24 часа')
plt.xlabel('Время')
plt.ylabel('Температура (°C)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()