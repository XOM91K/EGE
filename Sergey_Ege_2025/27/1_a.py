import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1_a.txt')]
clusters = [[], []]
for x in l:
    if x[1] > 3:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
ind = 0
centroids = [[], []]
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += math.dist(y, z)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
print(centroids)
Px = (centroids[0][0] + centroids[1][0]) / 2 * 10000
Py = (centroids[0][1] + centroids[1][1]) / 2 * 10000
print(int(Px), int(Py))