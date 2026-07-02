import math
l = [[d for d in x.split()] for x in open('12_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',', '.')), float(l[x][1].replace(',', '.')), l[x][2]]
clusters = [[], [], []]
for point in l:
    if point[0] > 20:
        clusters[0].append(point)
    elif point[1] > 22:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        mn_rast = 0
        for point in cluster:
            mn_rast += math.dist(centroid[:-1], point[:-1])
        if mn_rast < mn_sm_rast:
            mn_sm_rast = mn_rast
            centroids[ind] = centroid
    ind += 1
sr_rast1 = []
for p in clusters[0]:
    if p[2][2:] == 'II':
        sr_rast1.append(math.dist(centroids[0][:-1], p[:-1]))
sr_rast2 = []
for p in clusters[1]:
    if p[2][2:] == 'II':
        sr_rast2.append(math.dist(centroids[1][:-1], p[:-1]))
print(int(sum(sr_rast1) / len(sr_rast1) * 10000), int(sum(sr_rast2) / len(sr_rast2) * 10000))