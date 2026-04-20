import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('8_b.txt')]
clusters = [[], [], []]
for p in l:
    if 7 <= p[1] <= 31:
        if p[1] < 19:
            clusters[0].append(p)
        elif p[0] > 18:
            clusters[1].append(p)
        else:
            clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1, p2)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1

ct = 0
for p in l:
    dst = math.dist(p, centroids[0])
    if dst <= 10:
        ct += 1
ct2 = 0
for p in l:
    dst = math.dist(p, centroids[1])
    if dst > 5:
        ct2 += 1
print(ct, ct2 - 3)