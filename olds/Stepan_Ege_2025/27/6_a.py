a = [[float(j.replace(',','.')) for j in i.split()]for i in open("6_b.txt")]
clusters = [[], [], [], []]
for i in a:
    if i[0] < -3:
        clusters[0].append(i)
    elif i[1] < 0:
        clusters[1].append(i)
    elif i[1] < 9:
        clusters[2].append(i)
    else:
        clusters[3].append(i)
centroids = [[], [], [], []]
ind = 0
import math
for i in clusters:
    print(i[:5])
    mn_sm_rast = 10 ** 10
    for j in i:
        sm_rast = 0
        for z in i:
            sm_rast += math.dist(j, z)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = j
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000))
print(Px, Py)