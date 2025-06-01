l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_b.txt')]
clusters = [[], [], [], [], []]
for x in l:
    if x[1] <= 35 and x[0] < -35:
        clusters[0].append(x)
    elif x[0] > 0 and x[1] < 35:
        clusters[1].append(x)
    elif -30 <= x[0] <= -7 and x[1] < 35:
        clusters[2].append(x)
    elif x[1] > 45 and x[0] > -15:
        clusters[3].append(x)
    elif x[1] > 45 and -40 <= x[0] <= -23:
        clusters[4].append(x)
centroids = [[], [], [], [], []]
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
for x in clusters:
    print(x[:5])
Tx = int(abs(((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000)))
Ty = int(abs(((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5 * 10000)))
print(Tx, Ty)