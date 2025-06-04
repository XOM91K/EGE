l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_a.txt')]
clusters = [[], [], []]
for x in l:
    if x[1] > 0:
        clusters[0].append(x)
    elif x[0] > 2:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
del clusters[2]
import math
centroids = [[], []]
ind = 0
for x in clusters:
    mx_sm_rast = 0
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += math.dist(y, z)
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
print(centroids)
Tx = int((centroids[0][0] + centroids[1][0]) / 2 * 10000)
Ty = int((centroids[0][1] + centroids[1][1]) / 2 * 10000)
print(Tx, Ty)