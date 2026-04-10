import math
l = [[d for d in x.split()] for x in open('12_a.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
cl = [[], []]
for p in l:
    if p[1] > 8:
        cl[0].append(p)
    else:
        cl[1].append(p)
ctr = [[], []]
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
for x in l:
    if x[-1][0] == 'Y' and x[-1][2:] == 'III':
        mn_rast.append(math.dist([7.0391548, 12.3587258], x[:-1]))
print(int(min(mn_rast) * 10000))
print(int(max(mn_rast) * 10000))