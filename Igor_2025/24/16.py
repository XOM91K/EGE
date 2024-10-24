import re
s = open('16.txt').readline()
m = re.findall(r'[A-Z](\d+[02468])[A-Z]', s)
print(m)
print(max(m, key=lambda d: int(d)))