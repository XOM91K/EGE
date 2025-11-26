import re
s = open(r'C:\Users\Zarif\Downloads\731_1 (7).txt').readline()
m = re.findall(r'[^AB]*A[^AB]*B[^AB]*|[^AB]*B[^AB]*A[^AB]*', s)
print(len(max(m, key=len)))