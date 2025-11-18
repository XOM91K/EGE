import re
s = open(r'C:\Users\Zarif\Downloads\340_1 (7).txt').readline()
m = re.findall(r'[AEIUYO][^AEOIUY]', s)
print(m)