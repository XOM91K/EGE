import re
t=open('1').readline()
m=re.findall(r'[A-z.0-9]+@(?:yandex.ru|gmail.com)', t)
print(len(max(m, key=len)))
print((max(m, key=len)))