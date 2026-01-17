import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (15).txt').readline()
m = re.findall(r'(?:O[ABCDE]*F?[ABCDE]*F?[ABCDE]*)+O', s)
print(len(max(m, key=len)))