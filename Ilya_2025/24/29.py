import re
s = open(r'C:\Users\Zarif\Downloads\731_1 (1).txt').readline()
m = re.findall(r"[C-Z]*A[C-Z]*B[C-Z]*|[C-Z]*B[C-Z]*A[C-Z]*", s)
print(len(max(m, key=len)))