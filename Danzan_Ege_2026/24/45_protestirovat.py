import re
s = open(r'C:\Users\Zarif\Downloads\1647_1 (3).txt').readline()
m = re.findall(r'(?=((?:(?:[1-9][0-9]*|0)[+*])+(?:[1-9][0-9]*|0)))', s)
ch = []
for x in m:
    if eval(x) % 2 == 0:
        ch.append(x)
print(len(max(ch, key=len)))