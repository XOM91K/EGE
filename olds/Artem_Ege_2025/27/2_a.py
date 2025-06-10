l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], []]
for x in l:
    if x[1] > 18:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
centroids = [[], []]
ind = 0
import math
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
Px = (centroids[0][0] + centroids[1][0]) / 2 * 10000
Py = (centroids[0][1] + centroids[1][1]) / 2 * 10000
print(abs(int(Px)), abs(int(Py)))