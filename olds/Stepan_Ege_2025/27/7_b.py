l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7_b.txt')]
clusters = [[], [], []]
for x in l:
    if 21 <= x[1] <= 26:
        clusters[0].append(x)
    elif 16 <= x[1] <= 21:
        clusters[1].append(x)
    elif 5 <= x[1] <= 10:
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
for x in clusters:
    print(len(x))
Qx = abs(centroids[0][0] - centroids[2][0]) * 10000
Qy = abs(centroids[0][1] - centroids[2][1]) * 10000
print(int(abs(Qx)), int(abs(Qy)))