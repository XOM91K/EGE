import math
l = [[d for d in x.split()] for x in open('13_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
clusters = [[], [], []]
for p in l:
    if p[1] < 15:
        clusters[0].append(p)
    elif p[1] > 22:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
mn_rast = []
for cluster in clusters:
    for p1 in cluster:
        for p2 in cluster:
            if p1[-1][0] == 'Z' and p1[-1][2:] == 'I':
                if p2[-1][0] == 'Z' and p2[-1][2:] == 'I':
                    if math.dist(p1[:-1], p2[:-1]) != 0:
                        mn_rast.append(math.dist(p1[:-1], p2[:-1]))
ind = 0
ctJelt = [0, 0, 0]
for cluster in clusters:
    for p in cluster:
        if p[-1][0] == 'Z' and p[-1][2:] == 'I':
            ctJelt[ind] += 1
    ind += 1
print(ctJelt)
print(int(abs(min(mn_rast) * 10000)), int(abs(math.dist(centroids[2][:-1], centroids[0][:-1]) * 10000)))
