import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_b.txt')]
clusters = [[], [], [], [], []]
for point in l:
    if point[0] > 28:
        clusters[0].append(point)
    elif point[0] < 6.5:
        clusters[1].append(point)
    elif point[1] > 10:
        clusters[2].append(point)
    elif point[1] > 5:
        clusters[3].append(point)
    else:
        clusters[4].append(point)
for cluster in clusters:
    print(len(cluster))
centroids = [[], [], [], [], []]
ind = 0
# for cluster in clusters:
#     mn_sm_rast = 10 ** 10
#     for centroid in cluster:
#         sm_rast = 0
#         for point in cluster:
#             sm_rast += math.dist(centroid, point)
#         if sm_rast < mn_sm_rast:
#             mn_sm_rast = sm_rast
#             centroids[ind] = centroid
#     ind += 1
# Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000)
# Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5 * 10000)
# print(Px, Py)