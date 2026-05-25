import requests, re
url = 'http://ctfinf.ru:10019/'
session = requests.session()
for x in range(100):
    get = session.get(url)
    m = re.findall(r'center;">(.+?)</div>', get.content.decode(), flags=re.DOTALL)
    m = m[0].strip()
    print(m)
    m = eval(m)
    print(m)
    dt = {'answer': m}
    post = session.post(url, data=dt)
    print(post.text)
get = session.get(url)
print(get.text)