#6905
import re
s = open('14.txt').readline()
# m = re.findall(r'8[KNLF]+8', s)
# print(len(max(m, key=len)))
s = s.replace('N', 'K')
s = s.replace('L', 'K')
s = s.replace('F', 'K')
mx2 = 0
for x in '02468':
    mx = 0
    d = s.split(x)
    for y in d:
        if len(y) > 0 and y.count('K') == len(y):
            mx = max(mx, len(y))
    mx2 = max(mx2, mx)
print(mx2)
