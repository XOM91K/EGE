l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_a.txt')]
clusters = [[], [], []]
for x in l:
    if 0.2 <= x[1] <= 6.5 and x[0] > -1:
        clusters[0].append(x)
    elif x[0] < 0 and x[1] < 1:
        clusters[1].append(x)
    elif x[0] > 0.5 and -5 <= x[1] <= 1:
        clusters[2].append(x)
centroids = [[], [], []]
ind = 0
import math
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
Tx = int(abs(((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)))
Ty = int(abs(((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)))
print(Tx, Ty)