import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_a.txt')]
cl = [[], [], []]
for p in l:
    if p[1] > 5.5:
        cl[0].append(p)
    elif p[1] < 3:
        cl[1].append(p)
    else:
        cl[2].append(p)
ctr = [[], [], []]
rad = [0, 0, 0]
i = 0
for c in cl:
    mn_sm_rast = 10 ** 10
    for p1 in c:
        mx_rast = 0
        sm_rast = 0
        for p2 in c:
            mx_rast = max(mx_rast, math.dist(p1, p2))
            sm_rast += math.dist(p1, p2)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            ctr[i] = p1
            rad[i] = mx_rast
    i += 1
print(ctr)
print(rad)
Px = int(min(rad) * 10000)
Py = int(max(rad) * 10000)
print(Px, Py)