import math
l = [x.replace(',','.').split() for x in open('15_b.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
clusters = [[], [], []]
for p in l:
    if p[1] < 30:
        clusters[0].append(p)
    elif p[0] > 16:
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
        for p in cluster:
            sm_rast += math.dist(centroid[:-1], p[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
c = [0, 0, 0]
for x in range(3):
    for p in clusters[x]:
        if p[2][0] == 'K' and p[2][2:] == 'III':
            c[x] += 1
print(c)
mx_rast = []
for x in range(3):
    for p1 in clusters[x]:
        for p2 in clusters[x]:
            if p1[2][0] == 'G' and p1[2][2:] == 'V' and p2[2][0] == 'G' and p2[2][2:] == 'V':
                mx_rast.append(math.dist(p1[:-1], p2[:-1]))
print(int(math.dist(centroids[0][:-1], centroids[1][:-1]) * 10000), int(max(mx_rast) * 10000))

# mx_rast = []
# for p in clusters[1]:
#     if p[-1][0] == 'M' and p[-1][2:] == 'III':
#         mx_rast.append(math.dist(p[:-1], centroids[1][:-1]))
# kr = []
# for p in clusters[1]:
#     if p[-1][0] == 'M' and p[-1][2:] == 'III':
#         if math.dist(p[:-1], centroids[1][:-1]) == max(mx_rast):
#             kr = p
# print(int(kr[0] * 10000), int(kr[1] * 10000))