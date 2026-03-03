import re
s = open(r'C:\Users\Zarif\Downloads\1647_1 (1).txt').readline()
m = re.findall(r'(?:(?:[1-9][0-9]*|0)[+*]){31}(?:[1-9][0-9]*|0)', s)
mm = []
for x in m:
    if eval(x) % 2 == 0:
        mm.append(x)
print(len(max(mm, key=len)))
print((max(mm, key=len)))
