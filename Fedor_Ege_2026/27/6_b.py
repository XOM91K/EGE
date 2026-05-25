import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_b.txt')]
clusters = [[], [], []]
for x in l:
    if x[1] > 23:
        clusters[0].append(x)
    elif x[0] > 24:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
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
#print(int((math.dist(centroids[0], [1.0, 1.5]) + math.dist(centroids[1], [1.0, 1.5])) * 10000))
ct = 0

for p in clusters[2]:
    if math.dist(centroids[2], p) <= 1.2:
        ct += 1
mn_rast = []
for p in clusters[0]:
    if p != centroids[0]:
        mn_rast.append(math.dist(p, centroids[0]))
print(ct - 1, int(min(mn_rast) * 10000))