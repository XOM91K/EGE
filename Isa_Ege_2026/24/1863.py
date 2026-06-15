import re
s = open(r'C:\Users\Zarif\Downloads\1863_1 (2).txt').readline()
m = re.findall(r'(?:\d+\+){14}\d+', s)
print(len(max(m, key=len)))