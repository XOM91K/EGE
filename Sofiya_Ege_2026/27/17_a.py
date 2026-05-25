l = [[d for d in x.split()] for x in open('17_a.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',', '.')), float(l[x][1].replace(',', '.')), l[x][2]]
clusters = [[], []]
for point in l:
    if point[1] > 10:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
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
mn_rast = []
for x in range(2):
    for p1 in clusters[x]:
        if p1[-1] == 'VII':
            mn_rast.append(dist(centroids[x][:-1], p1[:-1]))
print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))
