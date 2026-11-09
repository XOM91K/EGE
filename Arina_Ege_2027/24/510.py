import re
s = open('/Users/zarif/Downloads/510_1.txt').readline()
m = re.findall(r'(?=((?:(?:[1-9][0-9]*|0)[+*])+(?:[1-9][0-9]*|0)))', s)
l = []
for x in m:
    if eval(x) == 0:
        l.append(x)
print(len(max(l, key=len)))

# 19 29 59 54 78  5 8