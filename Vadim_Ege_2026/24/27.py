import re
s = open(r'C:\Users\Zarif\Downloads\1458_1 (3).txt').readline()
m = re.findall(r'\((?:[0-9]+\+)+[0-9]+\)',s)
ln = []
for x in m:
    if eval(x[1:-1]) % 2 == 0:
        ln.append(len(x))
print(max(ln))