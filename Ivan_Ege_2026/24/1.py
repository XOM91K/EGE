import re
s = open('327_1 (10).txt').readline()
m = re.findall(r'[A-Z](\d*[02468])[A-Z]', s)
print(max(m, key=int))
# F7642289F