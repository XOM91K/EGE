import re
s = open(r'C:\Users\Zarif\Downloads\1458_1 (2).txt').readline()
m = re.findall('\((?:\d+\+)+\d+\)', s)

ln = []
for x in m:
    ev = eval(x)
    if ev % 2 == 0:
        ln.append(len(x))
print(max(ln))