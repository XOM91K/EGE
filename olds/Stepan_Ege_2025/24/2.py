import re
s = open(r'C:\Users\Zarif\Downloads\zadanie24_2 (1).txt').readline()
m = re.findall(r'(?:LDR)+(?:LD|L)?', s)
print(m)
print(len(max(m, key=len)))