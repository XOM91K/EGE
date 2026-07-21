import re
s = open('340_1 (16).txt').readline()
m = re.findall(r'[^AEOIUY]?(?:[AEOIUY][^AEOIUY])+[AEOIUY]?', s) # aeoiuy
print(max(m, key=len))
print(len(max(m, key=len)))