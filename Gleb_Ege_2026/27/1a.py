import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1a.txt')]
clusters = [[], []]
for point2 in l:
    if point2[1] > 3:
        clusters[0].append(point2)
    else:
        clusters[1].append(point2)
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
Px = int((centroids[0][0] + centroids[1][0]) / 2 * 10000)
Py = int((centroids[0][1] + centroids[1][1]) / 2 * 10000)
print(Px, Py)