import math
l = [x.replace(',','.').split() for x in open('12_a.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
clusters = [[], []]
for p in l:
    if p[1] > 10:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
ind = 0
centroids = [[], []]
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid[:-1], point[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
mn_rast = []
for x in range(2):
    for p in clusters[x]:
        if centroids[x] != p:
            if p[2] == 'VII':
               mn_rast.append(math.dist(p[:-1], centroids[x][:-1]))
print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))