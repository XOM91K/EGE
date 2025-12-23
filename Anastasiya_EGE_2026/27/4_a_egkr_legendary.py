import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_a_egkr_l.txt')]
clusters = [[], []]
for point in l:
    if point[1] > 8:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid, point)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
rast1 = int(10000 * math.dist([1.0, 1.0], centroids[1]))
rast2 = int(10000 * math.dist([1.0, 1.0], centroids[0]))
print(rast1, rast2)