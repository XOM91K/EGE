l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_b.txt')]
clusters = [[], [], [], [], []]
for x in l:
    if x[1] > 2 and x[0] > -1:
        clusters[0].append(x)
    elif x[1] > 2 and x[0] < -1:
        clusters[1].append(x)
    elif x[0] < -3:
        clusters[2].append(x)
    elif x[0] < 0:
        clusters[3].append(x)
    else:
        clusters[4].append(x)
# for x in clusters:
#     print(len(x))
del clusters[1]
import math
centroids = [[], [], [], []]
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
Tx = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000)
Ty = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000)
print(Tx, Ty)