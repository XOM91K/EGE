import re
s = open(r'C:\Users\Zarif\Downloads\1124_1 (7).txt').readline()
m = re.findall(r'(?:(?:[1-9][0-9]*[50]|0)[+*])+(?:[1-9][0-9]*[50]|0)', s)
print(max(m, key = len))
print(len(max(m, key = len)))