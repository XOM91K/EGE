import re
s = open(r'C:\Users\Zarif\Downloads\1125_1 (1).txt').readline()
m = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(len(max(m, key=len)))