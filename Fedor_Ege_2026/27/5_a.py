import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('5_a.txt')]
clusters = [[], [], []]
for p in l:
    if p[0] < 0 and p[1] < 0:
        clusters[0].append(p)
    elif p[0] > 0.5 and -6 <= p[1] <= 0:
        clusters[1].append(p)
    elif 0 <= p[1] <= 7 and -1 <= p[0] <= 2:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mx_sm_rast = 0
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1, p2)
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
print(centroids)
Tx = int(abs((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Ty = int(abs((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Tx, Ty)