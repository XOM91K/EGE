import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_a.txt')]
clusters = [[], [], []]
for p in l:
    if p[1] > 0:
        clusters[0].append(p)
    elif p[0] > 1.5:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
krayoyds = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mx_sm_rast = 0
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1, p2)
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            krayoyds[ind] = p1
    ind += 1
Tx = int((krayoyds[0][0] + krayoyds[1][0]) / 2 * 10000)
Ty = int((krayoyds[0][1] + krayoyds[1][1]) / 2 * 10000)
print(Tx, Ty)