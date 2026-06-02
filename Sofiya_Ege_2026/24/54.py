import re
s = open('54.txt').readline()
print(s.count('2401'))
m = re.findall(r'\d+', s)
mx = []
for x in m:
    if sum(map(int, x)) ** len(x) == int(x):
        mx.append(int(x))
print(max(mx))