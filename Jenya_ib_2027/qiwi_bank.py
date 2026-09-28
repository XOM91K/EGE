# import requests
# s = requests.Session()
# url = 'https://0a3c15c6-87e6-4074-8b15-e7826c464910.ctf.ctfinf.ru'
# for x in range(1, 10000):
#     gt = s.post(url, data={'auth': 'true', 'code': str(x)})
#     if 'Неверный код' not in gt.text:
#         print(x)
#         break
#     if x % 100 == 0:
#         print('сейчас перебираю: ', x)
s = r'|v{}aBUHEW{in\x7fhg'
for x in s:
    print(chr(ord(x) ^ 26), end='')