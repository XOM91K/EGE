import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7.txt')]
clusters = [[], []]
for point in l:
    if point[1] > 10:
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
print(int(math.dist([1, 1], centroids[1]) * 10000))
print(int(math.dist([1, 1], centroids[0]) * 10000))