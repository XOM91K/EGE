import math
l = [[float(d.replace (',', '.')) for d in x.split()] for x in open('5_b.txt')]
clusters = [[], [], [], [], []]
for point in l:
    if -30 < point[0] < -5.5 and point[1] < 40:
        clusters[0].append(point)
    elif point[0] > 0 and point[1] < 40:
        clusters[1].append(point)
    elif -55 < point[0] < -35 and point[1] < 40:
        clusters[2].append(point)
    elif -15 < point[0] < 10 and point[1] > 40:
        clusters[3].append(point)
    elif -40 < point[0] < -20 and point[1] > 40:
        clusters[4].append(point)
centroids = [[], [], [], [], []]
ind = 0
for cluster in clusters:
    mx_sm_rast = 0
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(point, centroid)
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
Tx = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0])/5 * 10000))
Ty = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1])/5 * 10000))
print(Tx, Ty)