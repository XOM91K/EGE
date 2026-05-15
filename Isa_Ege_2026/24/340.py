import re
s = open(r'C:\Users\Zarif\Downloads\340_1 (15).txt').readline()
m = re.findall(r'[^AEOIUY]?(?:[AEOIUY][^AEOIUY])+[AEOIUY]?', s)
print(max(m, key=len))
print(len(max(m, key=len)))