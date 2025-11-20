import re
s = open(r'C:\Users\Zarif\Downloads\146_1 (11).txt').readline()
m = re.findall(r'\d+', s)
print(m)
mx = []
for x in m:
    if sum(map(int, x)) ** len(x) == int(x):
        mx.append(int(x))
print(max(mx))
print(s.count('2401'))
print(m.count('2401'))