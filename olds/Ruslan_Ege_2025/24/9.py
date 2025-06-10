import re
s = open(r'327_1 (1).txt').readline()
m = re.findall(r'[A-Z](\d+[02468])[A-Z]', s)
print(max(m, key=int))