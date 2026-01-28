l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1.txt')]
clusters = [[], []]
for point in l:
    if point[1] > 3:
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
            sm_rast += ((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
Px = int((centroids[0][0] + centroids[1][0]) / 2 * 10000)
Py = int((centroids[0][1] + centroids[1][1]) / 2 * 10000)
print(Px, Py)