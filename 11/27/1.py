import math
# 1899
l = [x.replace(',','.').split() for x in open('1')]
l = [[float(x[0]), float(x[1]), x[2]] for x in l]
clusters = [[], []]
for p in l:
    if p[1] > 10:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
mn_rast = []
for x in range(2):
    for p in clusters[x]:
        if p[2][0] == 'N' and p[2][2:] == 'IV':
            mn_rast.append(math.dist(centroids[0 if x == 1 else 1][:-1], p[:-1]))
    print('-----------------------------')
print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))