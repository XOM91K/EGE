# import math
# l = [x.split() for x in open('5_a.txt')]
# l = [[float(d[0]), float(d[1]), d[2]] for d in l]
# clusters = [[], []]
# for p in l:
#     if p[1] > 15:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centroids = [[], []]
# ind = 0
# for cluster in clusters:
#     print(len(cluster))
#     mn_sm_rast = 10 ** 10
#     for centroid in cluster:
#         sm_rast = 0
#         for point in cluster:
#             sm_rast += math.dist(centroid[:2], point[:2])
#         if sm_rast < mn_sm_rast:
#             mn_sm_rast = sm_rast
#             centroids[ind] = centroid
#     ind += 1
# bl = []
# rast = 10 ** 7
# for p in clusters[1]:
#     if p[2] == 'VII':
#         if math.dist(p[:2], centroids[1][:2]) < rast:
#             rast = math.dist(p[:2], centroids[1][:2])
#             bl = p
# print(int(bl[0] * 10000), int(bl[1] * 10000))
import math
l = [x.split() for x in open('5_b.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
clusters = [[], [], []]
for p in l:
    if p[0] > 16:
        clusters[0].append(p)
    elif p[1] < 30:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid[:2], point[:2])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
ct_or = [0, 0, 0]
for x in range(3):
    for p in clusters[x]:
        if p[2][0] == 'K' and p[2][2:] == 'III':
            ct_or[x] += 1
mx_rast = 0
for p1 in l:
    for p2 in l:
        if p1[2][0] == 'G' and p1[2][2:] == 'V' and p2[2][0] == 'G' and p2[2][2:] == 'V':
            mx_rast = max(mx_rast, math.dist(p1[:2], p2[:2]))

ct_or = [0, 0, 0]
print(int(math.dist(centroids[0][:2], centroids[2][:2]) * 10000), int(mx_rast * 10000))
# bl = []
# rast = 10 ** 7
# for p in clusters[1]:
#     if p[2] == 'VII':
#         if math.dist(p[:2], centroids[1][:2]) < rast:
#             rast = math.dist(p[:2], centroids[1][:2])
#             bl = p
# print(int(bl[0] * 10000), int(bl[1] * 10000))