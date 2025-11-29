import re
s = open(r'C:\Users\Zarif\Downloads\390_1 (8).txt').readline()
m = re.findall(r'[AEOIUY]?(?:[^AEOIUY][AEOIUY])+[^AEOIUY]?', s)
print(len(max(m, key=len)))