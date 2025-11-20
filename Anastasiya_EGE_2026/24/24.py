import re
s = open(r'C:\Users\Zarif\Downloads\327_1 (5).txt').readline()
m = re.findall(r'[A-Z](\d+[02468])[A-Z]', s)
print(m)