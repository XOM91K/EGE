import re
s = open('39.txt').readline()
m = re.findall(r'[\w0-9.]+[\w0-9]+(?:@gmail\.com|@yandex\.ru)', s)
print(len(max(m, key=len)))