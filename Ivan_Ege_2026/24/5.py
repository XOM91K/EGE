import re
s = open(r'C:\Users\Zarif\Downloads\146_1 (16).txt').readline()
m = re.findall(r'\d+', s)
mx = []
for x in m:
    if sum(map(int, x)) ** len(x) == int(x):
      mx.append(int(x))
print(max(mx))
print(s.count('2401'))