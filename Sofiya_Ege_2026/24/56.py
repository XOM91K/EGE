import re

t = open(r'C:\Users\Zarif\Downloads\24 (31).txt').readline()
t = t.split('BC')
mxln = []
for x in range(len(t) - 180):
    ln = 0
    for y in range(0, 181):
        ln += len(t[x + y])
    mxln.append(ln)
print(max(mxln) + 360 + 2)
# t = t.replace('BC', '#')
# m = re.findall(r'(?:[^#]*#){180}[^#]*', t)
# print(len(m))
# print(len(max(m, key=len)) + 180)
# print((max(m, key=len)))
