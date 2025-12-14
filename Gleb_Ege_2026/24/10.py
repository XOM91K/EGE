import re
a = []
s = open(r'C:\Users\Zarif\Downloads\987_1 (7).txt').readline()
m = re.findall(r'D[^AD]+A', s)
print(len(max(m, key=len)))
