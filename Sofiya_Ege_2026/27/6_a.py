l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_a.txt')]
clusters = [[], []]
for point in l:
    if point[1] > 15:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
acentroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    mx_sm_rast = 0
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += ((centroid[0] - point[0]) ** 2 + (centroid[1] - point[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            acentroids[ind] = centroid
    ind += 1
print(centroids)
print(acentroids)
Px = int(abs((centroids[0][0] + centroids[1][0]) / 2 * 10000))
Py = int(abs((acentroids[0][1] + acentroids[1][1]) / 2 * 10000))
print(Px, Py)