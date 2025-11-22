import re
s = open(r'C:\Users\Zarif\Downloads\146_1 (12).txt').readline()
m = re.findall(r'\d+', s)
mx = []
for x in m:
    if sum(map(int, x)) ** len(x) == int(x) and int(x) <= 10 ** 6:
        print(x)
        mx.append(x)
print(max(mx, key=int))
print(s.count('2401'))
# print(max(['19', '8', '12312123123123'], key=int))