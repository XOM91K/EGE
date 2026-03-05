import re
s = open(r'C:\Users\Zarif\Downloads\1513_1 (2).txt').readline()
m = re.findall(r'(?:[1-9]\d\d[+*])+[1-9]\d\d', s)
print(max(m, key=len))
print(len(max(m, key=len)))