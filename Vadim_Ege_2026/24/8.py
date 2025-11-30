import re
s = open(r'C:\Users\Zarif\Downloads\146_1 (14).txt').readline()
m = re.findall(r'\d+', s)
d = []
for x in m:
    if sum(map(int, x)) ** len(x) == int(x):
        d.append(int(x))
print(max(d))
print(s.count('2401'))