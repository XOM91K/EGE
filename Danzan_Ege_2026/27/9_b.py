import math
l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('9_b.txt')]
clusters = [[], [], []]
for p in l:
    if p[0] > 26:
        clusters[0].append(p)
    elif p[1] < 20:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(point, centroid)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
ct = 0
for x in clusters[1]:
    if math.dist(x, centroids[1]) <= 1.2:
        ct += 1
B1 = ct - 1
mn_rast = []
for x in clusters[2]:
    if x != centroids[2]:
        mn_rast.append(math.dist(x, centroids[2]))
print(B1, int(min(mn_rast) * 10000))