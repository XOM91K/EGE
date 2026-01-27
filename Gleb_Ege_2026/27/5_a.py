import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('5_a.txt')]
clusters = [[], []]
for point in l:
    if point[0] > 40:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
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
P1 = abs(int((centroids[1][0] + centroids[1][1]) * 10000))
P2 = abs(int((centroids[0][0] + centroids[0][1]) * 10000))
print(centroids)
print(P1, P2)