import re
s = open(r'C:\Users\Zarif\Downloads\827_1 (3).txt').readline()
m = re.findall(r'B(?:[1-6]+[-*])+[1-6]+', s)
print(len(max(m, key = len)))
print(max(m, key = len))