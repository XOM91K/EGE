import re
s = open('24.txt').readline()
m = re.findall(r'[\w\d.]+@(?:yandex\.ru|gmail\.com)', s)
print(max(m, key=len))
print(len(max(m, key=len)))