import re
s = open(r'C:\Users\Zarif\Downloads\987_1 (3).txt').readline()
m=re.findall(r'D[^AD]+A', s)
print(len(max(m, key=len)))
print(m)