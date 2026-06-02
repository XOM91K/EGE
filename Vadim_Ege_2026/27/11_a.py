import math
l = [x.replace(',','.').split() for x in open('11_a.txt')]
l = [[float(x[0]), float(x[1]), str(x[2])] for x in l]
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
mx_rast = []
for p in l:
    if p[2][:2] == 'L3':
        mx_rast.append(math.dist(centroids[0][:2], p[:2]))
mx_rast2 = []
for p in l:
    if p[2][:2] == 'L3':
        mx_rast2.append(math.dist(centroids[1][:2], p[:2]))
print(int(max(mx_rast) * 10000), int(max(mx_rast2) * 10000))