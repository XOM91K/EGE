import re
s = open(r'C:\Users\Zarif\Downloads\146_1 (13).txt').readline()
m = re.findall(r'\d+', s)
print(s.count('2401'))
mx = []
for x in m:
    if int(x) < 10 ** 6 and sum(map(int, x)) ** len(x) == int(x):
        mx.append(int(x))
print(max(mx))