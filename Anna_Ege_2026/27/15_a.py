import math
l = [x.replace(',','.').split() for x in open('15_a.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
clusters = [[], []]
for p in l:
    if p[1] > 15:
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
        for p in cluster:
            sm_rast += math.dist(centroid[:-1], p[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
mx_rast = []
for p in clusters[1]:
    if p[-1][0] == 'M' and p[-1][2:] == 'III':
        mx_rast.append(math.dist(p[:-1], centroids[1][:-1]))
kr = []
for p in clusters[1]:
    if p[-1][0] == 'M' and p[-1][2:] == 'III':
        if math.dist(p[:-1], centroids[1][:-1]) == min(mx_rast):
            kr = p
print(int(kr[0] * 10000), int(kr[1] * 10000))