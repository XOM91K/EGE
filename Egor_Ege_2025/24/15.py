import re
s = open(r'C:\Users\Zarif\Downloads\1124_1 (5).txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*[05]|5|0)[*+])+(?:[1-9]\d*[05]|5|0)', s)
print(max(m, key=len))
print(len(max(m, key=len)))