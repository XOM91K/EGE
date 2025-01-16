import re
s = open(r'C:\Users\Zarif\Downloads\510_1.txt').readline()
m = re.findall(r'(?:(?:[1-9]\d+|0)[+*])+(?:[1-9]\d+|0)', s)
l = []
for x in m:
    if eval(x) == 0:
        l.append(x)
print(max(l, key=len))
print(len(max(l, key=len)))