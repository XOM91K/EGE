import math
l = [x.replace(',','.').split() for x in open('13_a.txt')]
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
mx_rast1 = []
for p in l:
    if p[2][:2] == 'L3':
        mx_rast1.append(math.dist(p[:2], centroids[0][:2]))
mx_rast2 = []
for p in l:
    if p[2][:2] == 'L3':
        mx_rast2.append(math.dist(p[:2], centroids[1][:2]))
print(int(max(mx_rast1) * 10000), int(max(mx_rast2) * 10000))