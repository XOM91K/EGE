import requests
url = 'http://proginf.ru:19000/spin'
s = requests.session()
for x in range(1000):
    try:
        get = s.get(url).text
        if 'ctf' in get:
            print(get)
            break
        if x % 100 == 0:
            print(x)
    except:
        pass