import requests
import json
import matplotlib.pyplot as plt

# Отправляем GET-запрос на сайт
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=55.7522&longitude=37.6156&hourly=temperature_2m,wind_speed_10m&timezone=Europe%2FMoscow&forecast_days=1')

# Получаем JSON-данные из ответа

json_data = response.json()
print(json_data)
days = [d[-5:] for d in json_data['hourly']['time']]
tmp = json_data['hourly']['temperature_2m']
sp_wd = json_data['hourly']['wind_speed_10m']
x = [d for d in days]
y = [d for d in tmp]
y2 = [d for d in sp_wd]
plt.subplot(2, 1, 2)
plt.plot(x, y)
plt.xlabel('Погода за текущий день')
plt.ylabel('Температура')
plt.title('Температура')
plt.subplot(2, 1, 1)
plt.plot(x, y2)
plt.title('Скорость ветра')
plt.xlabel('Погода за текущий день')
plt.ylabel('Температура и скорость ветра')
plt.show()