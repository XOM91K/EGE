l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_b.txt')]
clusters = [[], [], []]
print(l)
for x in l:
    if x[1] > -1.5 and x[0] > -2:
        clusters[0].append(x)
    elif x[0] < -5:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
centroids = [[], [], []]
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

Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)