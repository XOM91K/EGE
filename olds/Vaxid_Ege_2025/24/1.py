import re
s = open(r'C:\Users\Zarif\Downloads\195_1 (6).txt').readline()
m = re.findall(r'[KNLF]+', s)
print(m)