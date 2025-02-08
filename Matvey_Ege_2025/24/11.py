import re
s = open('339_1 (5).txt').readline()
#m = re.findall(r'[DE]+F?[DE]+', s)
# print(len(max(m, key=len)))
# print(max(m, key=len))
s = s.split('F')
mxln = 0
for x in range(len(s) - 1):
    mxln = max(mxln, len(s[x] + s[x + 1]))
print(mxln + 1)