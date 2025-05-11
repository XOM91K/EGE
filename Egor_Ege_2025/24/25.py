import re
s = open(r'C:\Users\Zarif\Downloads\986_1 (2).txt').readline()
m = re.findall(r'(?:[^EYUIOA][A-Z][EYUIOA])+', s)
print(len(max(m, key=len)) / 3)