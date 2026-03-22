import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] > 22:
        clusters[0].append(point)
    elif point[0] > 24:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += ((point[0] - centroid[0]) ** 2 + (centroid[1] - point[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
ct = -1
for x in clusters[2]:
    if math.dist(x, centroids[2]) <= 1.2:
        ct += 1
print(ct)
mn_rast = 10 ** 10
for x in clusters[0]:
    if x != centroids[0]:
        mn_rast = min(mn_rast, math.dist(x, centroids[0]))
print(int(mn_rast * 10000))