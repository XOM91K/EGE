import re
s = open(r'C:\Users\Zarif\Downloads\1127_1 (11).txt').readline()
m = re.findall(r'AFD(?:[123456789]\d*|0)(?:[+*](?:[123456789]\d*|0))+', s)
print(len(max(m, key=len)))
print((max(m, key=len)))