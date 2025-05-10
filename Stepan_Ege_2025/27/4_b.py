l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_b.txt')]
clusters = [[], [], [], [], []]
for x in l:
    if -54 <= x[0] <= -36 and -33 <= x[1] <= 33:
        clusters[0].append(x)
    elif -27 <= x[0] <= -9 and -33 <= x[1] <= 33:
        clusters[1].append(x)
    elif 0 <= x[0] <= 18 and -33 <= x[1] <= 33:
        clusters[2].append(x)
    elif -12 <= x[0] <= 9 and 48 <= x[1] <= 108:
        clusters[3].append(x)
    elif -39 <= x[0] <= -21 and 42 <= x[1] <= 108:
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
print(centroids)
Tx = (centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000
Ty = (centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5 * 10000
print(int(abs(Tx)), int(abs(Ty)))
print()