import re
s = open(r'C:\Users\Zarif\Downloads\986_1 (5).txt').readline()
m = re.findall(r'(?:[^AEOIUY][A-Z][AEOIUY])+', s)
print(max(m, key=len))
print(len(max(m, key=len)))