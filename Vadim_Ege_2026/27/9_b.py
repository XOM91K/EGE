from math import *

l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('9_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] > 10 and point[1] < 20:
        clusters[0].append(point)
    elif point[0] < 18 and point[0] > 10:
        clusters[1].append(point)
    elif point[0] > 18 and point[0] < 25:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
clusters = sorted(clusters, key=len)
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += ((point[0] - centroid[0]) ** 2 + (centroid[1] - point[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
Q2 = 0
Q1 = 0
for p in l:
    if dist(p, centroids[2]) <= 10:
        Q1 += 1
for p in l:
    if dist(p, centroids[0]) > 5 and (p in clusters[0] or p in clusters[1] or p in clusters[2]):
        Q2 += 1
print(Q1, Q2)
