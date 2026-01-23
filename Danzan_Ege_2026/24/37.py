import re
s = open(r'C:\Users\Zarif\Downloads\1332_1 (2).txt').readline()
m = re.findall(r'(?:(?:[1-9][0-9]*|0)[-*])+(?:[1-9][0-9]*|0)', s)
print(len(max(m, key = len)), max(m, key = len))