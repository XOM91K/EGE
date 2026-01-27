import re
s = open(r'C:\Users\Zarif\Downloads\1565_1 (2).txt').readline()
m = re.findall(r'(?:CAB|BAC){24}', s)
print(len(max(m, key=len)))