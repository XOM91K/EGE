import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_b.txt')]
cl = [[], [], [], [], []]
for p in l:
    if p[0] > 4.2:
        cl[0].append(p)
    elif p[1] > 5.2:
        cl[1].append(p)
    elif p[0] < -1:
        cl[2].append(p)
    elif p[0] < 2:
        cl[3].append(p)
    else:
        cl[4].append(p)
ctr = [[], [], [], [], []]
rad = [0, 0, 0, 0, 0]
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