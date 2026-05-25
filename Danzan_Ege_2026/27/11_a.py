import math
l = [x.replace(',','.').split() for x in open('11_a.txt')]
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
for p in clusters[0]:
    if p[2] == 'VII':
        mn_rast.append(math.dist(p[:-1], centroids[0][:-1]))
for p in clusters[1]:
    if p[2] == 'VII':
        mn_rast.append(math.dist(p[:-1], centroids[1][:-1]))
print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))