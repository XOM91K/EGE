l = [[d for d in x.split()] for x in open('18_a.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',', '.')), float(l[x][1].replace(',', '.')), l[x][2]]
clusters = [[], []]
for point in l:
    if point[1] > 10:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
print(len(clusters[0]), len(clusters[1]))
centroids = [[], []]
ind = 0
from math import *

for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += dist(centroid[:-1], point[:-1])
        if mn_sm_rast > sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
d = []
d2 = []
for x in range(2):
    for p in clusters[x]:
        if p[2][:2] == 'L3':
            d.append(dist(centroids[0][:-1], p[:-1]))
            d2.append(dist(centroids[1][:-1], p[:-1]))
print(int(max(d) * 10_000), int(max(d2) * 10_000))
