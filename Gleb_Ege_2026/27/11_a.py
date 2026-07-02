import math
l = [[d for d in x.split()] for x in open('11_a.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
clusters = [[], []]
for point in l:
    if (point[0] > 3.5 and point[1] < 5) or (point[0] > 5):
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(point[:2], centroid[:2])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
A1 = 0
mn_rast = []
for x in range(2):
    for point in clusters[x]:
        if point[2][0] == 'K' and point[2][2:] == 'III':
           mn_rast.append(math.dist(point[:-1], centroids[x][:-1]))
print(int(min(mn_rast) * 10000), int((math.dist([-1.0, -2.0], centroids[0][:-1]) + math.dist([-1.0, -2.0], centroids[1][:-1])) * 10000))
print()