import math
l = [x.replace(',','.').split() for x in open('12_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0]), float(l[x][1]), l[x][2]]
clusters = [[], []]
for p in l:
    if p[1] > 15:
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
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
mn_rast = []
for p in clusters[1]:
    if p[2][0] == 'M' and p[2][2:] == 'III':
        mn_rast.append(math.dist(p[:-1], centroids[1][:-1]))
for p in clusters[1]:
    if p[2][0] == 'M' and p[2][2:] == 'III':
        if math.dist(p[:-1], centroids[1][:-1]) == min(mn_rast):
            print(int(p[0] * 10000), int(p[1] * 10000))