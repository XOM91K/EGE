import re
s = open('15.txt').readline()
m = re.findall(r'[C-Z]*A[C-Z]*B[C-Z]*|[C-Z]*B[C-Z]*A[C-Z]*', s)
print(max(m, key=len))
print(len(max(m, key=len)))