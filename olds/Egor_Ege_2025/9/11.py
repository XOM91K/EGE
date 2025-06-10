import math
l = [[int(d) for d in x.split()] for x in open('11.txt')]
cnt = 0
for x in l:
    pvtr = [i for i in x if x.count(i) == 2]
    nevtr = [y for y in x if x.count(y) == 1]
    if len(pvtr) == 4 and len(nevtr) == 2:
        if max(pvtr) ** 2 > nevtr[0] * nevtr[1]:
            cnt += 1
print(cnt)