import re
s = open(r'C:\Users\Zarif\Downloads\1265_1 (4).txt').readline()
m = re.findall(r'(?:(?:[7-9][0-9]*|0)[-*])+(?:[7-9][0-9]*|0)', s)
print(len(max(m, key = len)), max(m, key = len))