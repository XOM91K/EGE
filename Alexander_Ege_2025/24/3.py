import re
s = open(r'C:\Users\Zarif\Downloads\195_1 (5).txt').readline()
m = re.findall(r'8[KNLF]+8', s)
print(len(max(m, key=len)) - 2)
# 5103