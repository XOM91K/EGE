import re
s = open(r'C:\Users\Zarif\Downloads\1647_1 (6).txt').readline()
a = re.findall(r'(?=((?:[1-9]\d*[+*])+[1-9]\d*))', s)
a = sorted(a, key=len)[::-1]
for e in a:
    if eval(e) % 2 == 0:
        print(len(e))
        break

#23 + 22 + 22 + 22