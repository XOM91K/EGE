import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('5_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[0] > 10:
        if point[1] < 34:
            clusters[0].append(point)
        elif point[1] < 43:
            clusters[1].append(point)
        else:
            clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid, point)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
P1 = int(centroids[2][0] * 10000)
P2 = int(centroids[0][1] * 10000)
print(centroids)
print(P1, P2)