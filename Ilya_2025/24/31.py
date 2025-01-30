import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (12).txt').readline()
m = re.findall(r'(?:O[^F]*F?[^F]*F?[^F]*)+O', s)
print(len(max(m, key=len)))