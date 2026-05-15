import math
l = [[d for d in x.replace(',', '.').split()] for x in open('9_a.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0]), float(l[x][1]), l[x][2]]
clusters = [[], []]
for p in l:
    if p[1] > 10:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:2], p2[:2])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
rast = []
for p in l:
    if p[2][0] == 'Y' and p[2][2:] == 'III':
        rast.append(math.dist(centroids[0][:2], p[:2]))
print(int(min(rast) * 10000))
print(int(max(rast) * 10000))