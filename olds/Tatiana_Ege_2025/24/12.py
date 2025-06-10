import re
s = open(r'C:\Users\Zarif\Downloads\339_1 (5).txt').readline()
# m = re.findall(r'[DE]+F[DE]+', s)
# print(max(m, key=len))
# print(len(max(m, key=len)))
#38
s = s.split('F')
mxln = 0
for x in range(len(s) - 1):
    mxln = max(mxln, len(s[x]) + len(s[x + 1]))
print(mxln + 1)