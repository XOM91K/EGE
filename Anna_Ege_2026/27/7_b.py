import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] < 15:
        clusters[0].append(point)
    elif point[1] > 23:
        clusters[1].append(point)
    else:
        clusters[2].append(point)

centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster), '--------------------')
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid, point)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ct = 0
    for point in cluster:
        if math.dist(centroids[ind], point) <= 0.75:
            ct += 1
    print(ct)
    ind += 1
print(int(math.dist([1, 1], centroids[1]) * 10000))
print(int(math.dist([1, 1], centroids[0]) * 10000))