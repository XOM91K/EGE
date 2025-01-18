import re
import string
s = open(r'C:\Users\Zarif\Downloads\195_1 (2).txt').readline()
# match = re.findall(r'0[KNLF]*0|2[KNLF]*2|4[KNLF]*4|6[KNLF]*6|8[KNLF]*8', s)
# print(len(max(match, key = len)))
s = s.replace('K', '#')
s = s.replace('N', '#')
s = s.replace('L', '#')
s = s.replace('F', '#')
mxln = 0
for x in '02468':
    d = s
    d = d.split(x)
    for y in d:
        if len(y) == y.count('#'):
            mxln = max(mxln, len(y))
print(mxln)