import re
s = open(r'C:\Users\Zarif\Downloads\731_1 (2).txt').readline()
match = re.findall(r"[C-Z]*A[C-Z]*B[C-Z]*|[C-Z]*B[C-Z]*A[C-Z]*", s)
print(max(match, key=len))
print(len(max(match, key=len)))