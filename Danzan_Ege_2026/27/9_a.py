import math
l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('9_a.txt')]
clusters = [[], []]
for p in l:
    if p[1] < 11:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
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
print(centroids)
A1 = 344
A2 = int((math.dist(centroids[0], [1.0, 1.5]) + math.dist(centroids[1], [1.0, 1.5])) * 10000)
print(A1, A2)