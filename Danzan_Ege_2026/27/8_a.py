import math
l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('8_a.txt')]
clusters = [[], []]
for p in l:
    if p[0] < 78:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(point, centroid)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
print(len(clusters[0]), len(clusters[1]))
ct = 0
ct2 = 0
for p in l:
    if math.dist(p, centroids[0]) <= 0.7:
        ct += 1
for p in l:
    if math.dist(p, centroids[1]) >= 1.3:
        ct2 += 1
print(ct, ct2)