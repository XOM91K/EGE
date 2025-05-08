import re
s = open(r'C:\Users\Zarif\Downloads\987_1 (2).txt').readline()
m = re.findall(r'A[^AD]{271}D|D[^AD]{271}A', s)
#m = re.findall(r'A[^[AD]\d]+D|D[^[AD]\d]+A', s)
print(len(max(m, key=len)))
print(max(m, key=len))