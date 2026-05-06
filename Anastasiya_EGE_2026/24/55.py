import re

m = open(r'C:\Users\Zarif\Downloads\1600_1 (2).txt').readline()
s = re.findall(r'(?=((?:[1-9]+[+*]){49}[1-9]+))', m)
print(len(max(s, key=len)))
print(max(s, key=len))
