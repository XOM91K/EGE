import re
t=open(r'C:\Users\Zarif\Downloads\987_1 (6).txt').readline()
m=re.findall(r'D[^AD]+A', t)
print(len(max(m, key=len)))
print(m)