import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('5_b.txt')]
cl = [[], [], [], [], []]
for p in l:
    if p[0] < -1:
        cl[0].append(p)
    elif p[0] > 4:
        cl[1].append(p)
    elif p[1] > 5.2:
        cl[2].append(p)
    elif p[0] < 1.8:
        cl[3].append(p)
    else:
        cl[4].append(p)
ctr = [[], [], [], [], []]
rad = [0, 0, 0, 0, 0]
ind = 0
for c in cl:
    mn_sm_rast = 10 ** 10
    for p1 in c:
        sm_rast = 0
        mx_rast = 0
        for p2 in c:
            sm_rast += math.dist(p1, p2)
            mx_rast = max(mx_rast, math.dist(p1, p2))
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            rad[ind] = mx_rast
            ctr[ind] = p1
    ind += 1
print(ctr)
print(rad)
print(int(min(rad) * 10000), int(max(rad) * 10000))