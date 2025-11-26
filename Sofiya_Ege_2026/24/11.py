import re
t=open(r'C:\Users\Zarif\Downloads\340_1 (13).txt').readline()
m=re.findall(r'(?:[AEOIUY][^AEOIUY])+[AEOIUY]?|(?:[^AEOIUY][AEOIUY])+[^AEOIUY]', t)
print(len(max(m, key=len)))