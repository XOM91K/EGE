l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], [], [], []]
for point in l:
    if point[1] < 4:
        clusters[0].append(point)
    elif point[1] > 14:
        clusters[1].append(point)
    elif point[0] < 12:
        clusters[2].append(point)
    else:
        clusters[3].append(point)
centroids = [[], [], [], []]
ind = 0
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
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000)
print(Px, Py)