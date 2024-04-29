import re
s = open('10.txt').readline()
m = re.findall(r"[C-Z]+A[C-Z]*B[C-Z]+|[C-Z]+B[C-Z]*A[C-Z]+", s)
print(len(max(m, key=len)))