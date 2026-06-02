import math
l = [x.replace(',','.').split() for x in open('11_b.txt')]
l = [[float(x[0]), float(x[1]), str(x[2])] for x in l]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[0] > 22:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
ind = 0
centroids = [[], [], []]
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid[:-1], point[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
ct_s = [0, 0, 0]
s_z = []
for x in range(3):
    for p in clusters[x]:
        if p[2][0] == 'L':
            ct_s[x] += 1
            s_z.append(p)
print(ct_s)
mx_rast = []
for p1 in s_z:
    for p2 in s_z:
        mx_rast.append(int(math.dist(p1[:2], p2[:2]) * 10000))
print(int(math.dist(centroids[0][:2], centroids[1][:2]) * 10000), int(max(mx_rast)))