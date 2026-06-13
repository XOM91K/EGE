import re
s = open(r'C:\Users\Zarif\Downloads\1862_1 (2).txt').readline()
m = re.findall(r'(?=((?:[^A-F]*[A-F]){3}[^A-F]*))', s)
ln = []
for x in m:
    can = True
    for y in '0123456789':
        if y not in x:
            can = False
    if can:
        ln.append(x)
print(len(min(ln, key=len)))