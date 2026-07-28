import re
ct = 0
mx = []
s = open(r'C:\Users\Zarif\Downloads\146_1 (21).txt').readline()
m = re.findall(r'[1-9][0-9]{0,7}', s)
for x in range(len(m)):
    if sum(map(int, m[x])) ** len(m[x]) == int(m[x]):
        mx.append(int(m[x]))
print(max(mx))
print(s.count(str(max(mx))))