import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('8_a.txt')]
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
            sm_rast += math.dist(p1, p2)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
Px = int(min(math.dist([5.5, 9.1], centroids[0]), math.dist([5.5, 9.1], centroids[1])) * 10000)
new_tchk = [(centroids[0][0] + centroids[1][0]) / 2, (centroids[0][1] + centroids[1][1]) / 2]
Py = int(math.dist([5.5, 9.1], new_tchk) * 10000)
print(Px, Py)
# ct = 0
# for p in l:
#     dst = math.dist(p, centroids[1])
#     if dst <= 10:
#         ct += 1
# ct2 = 0
# for p in l:
#     dst = math.dist(p, centroids[0])
#     if dst > 5:
#         ct2 += 1
# print(ct, ct2)