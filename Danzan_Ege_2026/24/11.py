import re
s = open(r'C:\Users\Zarif\Downloads\986_1 (4).txt').readline()
m = re.findall(r'(?:[^AEOIUY]\w[AO])+', s)
print(len(max(m, key=len)))