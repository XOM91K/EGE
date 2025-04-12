import re
s = open(r'C:\Users\Zarif\Downloads\1172_1 (3).txt').readline()
r = re.findall(r"(?:(?:[1-9]\d*|0)[*+])+(?:[1-9]\d*|0)", s)
mx = 0
for x in r:
    mx = max(mx, x.count('*') + x.count('+') + 1)
    if mx == 52:
        print(x)
        break
print(mx)