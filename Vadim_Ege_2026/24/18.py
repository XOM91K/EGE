import re
s = open(r'C:\Users\Zarif\Downloads\1414_1 (6).txt').readline()
s = s.split('T')
mx = []
for x in range(len(s) - 100):
    ln = 0
    for y in range(0, 101):
        ln += len(s[x + y])
    mx.append(ln)
print(max(mx) + 100)
# m = re.findall(r'(?:[^T]*T){100}[^T]*', s)
# print(len(max(m, key=len)))