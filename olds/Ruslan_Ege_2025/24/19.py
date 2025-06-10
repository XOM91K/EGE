import re
s = open(r'C:\Users\Zarif\Downloads\987_1.txt').readline()
m = re.findall(r'D[^AD]+A', s)
print(max(m, key=len))
print(len(max(m, key=len)))