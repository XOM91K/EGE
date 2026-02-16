import re
s = open(r'C:\Users\Zarif\Downloads\1332_1 (3).txt').readline()
m = re.findall(r'(?:(?:[7-9][0-9]*|0)[-*])+(?:[7-9][0-9]*|0)', s)
print(max(m, key=len))
print(len(max(m, key=len)))