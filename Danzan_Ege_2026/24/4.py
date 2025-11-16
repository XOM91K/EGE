import re
s = open(r'C:\Users\Zarif\Downloads\zadanie24_1 (1).txt').readline()
m = re.findall(r'A+', s)
print(len(max(m, key=len)))