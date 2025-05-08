import re
s = open(r'C:\Users\Zarif\Downloads\827_1 (1).txt').readline()
m = re.findall(r'B(?:\d+[*-])+\d+', s)
print(max(m, key=len))
print(len(max(m, key=len)))