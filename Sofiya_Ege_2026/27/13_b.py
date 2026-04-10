import math
l = [[d for d in x.split()] for x in open('13_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
cl = [[], [], []]
for p in l:
    if p[1] > 22:
        cl[0].append(p)
    elif p[1] > 16:
        cl[1].append(p)
    else:
        cl[2].append(p)
ctr = [[], [], []]
ind = 0
for c in cl:
    print(len(c))
    mn_sm_rast = 10 ** 10
    for p1 in c:
        sm_rast = 0
        for p2 in c:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            ctr[ind] = p1
    ind += 1
print(ctr)
mn_rast = []
for c in cl:
    ct = 0
    for p1 in c:
        if p1[-1][0] == 'Z' and p1[-1][2:] == 'IV':
            ct += 1
        for p2 in c:
            if p1[-1][0] == 'Z' and p1[-1][2:] == 'IV' and p2[-1][0] == 'Z' and p2[-1][2:] == 'IV':
                mn_rast.append(math.dist(p1[:-1], p2[:-1]))
    print('кол-во сверхг:', ct)
mn_rast = sorted(mn_rast)
print(mn_rast)
print(int((0.18251395034202345 * 10000)))
print(int(math.dist(ctr[0][:-1], ctr[2][:-1]) * 10000))