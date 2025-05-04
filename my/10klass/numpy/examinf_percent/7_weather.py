import requests
import matplotlib.pyplot as plt
# 1. Получаем данные о погоде через API
def get_weather(city):
    api_key = "80859c968f5e35887f0055bb206183eb"  # Можно получить бесплатно на openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
# 2. Собираем данные для нескольких городов
cities = ['Moscow', 'London', 'New York', 'Tokyo', 'Dubai']
temperatures = []
for city in cities:
    data = get_weather(city)
    if data['cod'] == 200:  # Проверка успешного запроса
        temp = data['main']['temp']
        temperatures.append(temp)
        print(f"{city}: {temp}°C")
    else:
        print(f"Ошибка для города {city}")
        temperatures.append(None)
# 3. Строим простой график
plt.figure(figsize=(10, 5))
plt.bar(cities, temperatures, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Текущая температура в крупных городах')
plt.ylabel('Температура (°C)')
plt.grid(axis='y', linestyle='--')
plt.show()

