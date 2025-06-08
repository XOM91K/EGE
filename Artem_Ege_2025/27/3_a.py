l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_a.txt')]
clusters = [[], [], []]
for x in l:
    if 1 <= x[1] <= 7 and -1 <= x[0] <= 2:
        clusters[0].append(x)
    elif x[1] < 0 and x[0] < 0:
        clusters[1].append(x)
    elif 0.5 <= x[0] <= 3.5 and -6 <= x[1] <= 0:
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
Tx = int(abs((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Ty = int(abs((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Tx, Ty)