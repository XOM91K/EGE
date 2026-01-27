l = [[float(d.replace(',','.')) for d in x.split()] for x in open('8_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[0] > 10:
        if point[1] > 42:
            clusters[0].append(point)
        elif point[1] > 33:
            clusters[1].append(point)
        else:
            clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += ((centroid[0] - point[0]) ** 2 + (centroid[1] - point[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
Qx = int(centroids[0][0] * 10000)
Qy = int(centroids[2][1] * 10000)
print(Qx, Qy)