import re
s = open(r'C:\Users\Zarif\Downloads\1171_1 (1).txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*|0)[*-])+(?:[1-9]\d*|0)', s)
print(max(m, key=len))
print(len(max(m, key=len)))