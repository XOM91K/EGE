l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('4_a.txt')]
clusters = [[], [], [], []]
for x in l:
    if x[0] < 0:
        clusters[0].append(x)
    elif x[1] < 0 :
        clusters[1].append(x)
    elif x[1] > 9:
        clusters[2].append(x)
    else:
        clusters[3].append(x)

centroids = [[], [], [],[]]
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
print(centroids)
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000)
print(abs(int(Px)), abs(int(Py)))