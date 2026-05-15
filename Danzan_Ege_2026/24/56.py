import re
s = open(r'C:\Users\Zarif\Downloads\390_1 (10).txt').readline()
m = re.findall(r'(?:[^AOEUYI][AOEUYI])+[^AOEUYI]?', s)
print(max(m, key=len), len(max(m, key=len)))