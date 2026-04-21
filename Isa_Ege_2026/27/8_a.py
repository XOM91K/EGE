import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('8_a.txt')]
clusters = [[], []]
for p in l:
    if p[1] > 15:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1, p2)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
ct = 0
for p in clusters[0]:
    if p[1] < centroids[0][1]:
        ct += 1
A1 = ct
A2 = abs(int((centroids[1][0] - centroids[0][0]) * 10000))
print(A1, A2)