l = [[int(d) for d in x.split()] for x in open('6.txt')]
import math
s = 6089572
old_sm = 10 ** 100
for i in range(13500, len(l)):
    sm = 0
    for j in l:
        if abs(l[i][0] - j[0]) > s / 2:
            sm += (s - abs(l[i][0] - j[0])) * math.ceil(j[1] / 11)
        else:
            sm += abs(l[i][0] - j[0]) * math.ceil(j[1] / 11)
    if sm < old_sm:
        print(sm, '----')
    else:
        print(sm, '++++')
    old_sm = sm