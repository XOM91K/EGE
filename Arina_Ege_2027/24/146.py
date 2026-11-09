import re
s = open('/Users/zarif/Downloads/146_1.txt').readline()
m = re.findall(r'\d+', s)
l = []
for x in m:
    if sum(map(int, x)) ** len(x) == int(x):
        l.append(int(x))
print(max(l))
print(s.count('2401'))