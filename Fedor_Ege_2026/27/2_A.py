import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_A.txt')]
clusters = [[], []]
for p in l:
    if p[1] > 0:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
ind = 0
centroids = [[], []]
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1, p2)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0]) / 2 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1]) / 2 * 10000))
print(Px, Py)