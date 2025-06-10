import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (11).txt').readline()
m = re.findall(r'(?:O[A-E]*F?[A-E]*F?[A-E]*)+O', s)
print(len(max(m, key=len)))