import math
l = [x.replace(',','.').split() for x in open('15_a.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
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
mn = []
ind = 1
for x in range(2):
    for p in clusters[x]:
        if p[2][0] == 'N' and p[2][2:] == 'IV':
            mn.append(math.dist(p[:-1], centroids[ind][:-1]))
    ind -= 1

print(int(min(mn) * 10000), int(max(mn) * 10000))