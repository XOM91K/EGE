import math
d = 123
l = [[int(d) for d in x.split()] for x in open('23.txt')]
old_sm = 10 ** 100
for i in range(100100, len(l)):
    sm = 0
    for j in range(len(l)):
        sm += abs(l[i][0] - l[j][0]) * math.ceil(l[j][1] / d)
    if sm < old_sm:
        print(sm, '---')
    else:
        print(sm, '+++')
    old_sm = sm