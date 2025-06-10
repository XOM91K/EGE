import re
s = open(r'C:\Users\Zarif\Downloads\390_1 (2).txt').readline()
m = re.findall(r'[^AEOIUY]?(?:[AEOIUY][^AEOIUY])+[AEOIUY]?', s)
print(len(max(m, key=len)))