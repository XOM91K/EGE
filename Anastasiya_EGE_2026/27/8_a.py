l = [[float(d.replace(',','.')) for d in x.split()] for x in open('8_a.txt')]
clusters = [[], []]
for point in l:
    if point[0] < 40:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
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
P1 = int((centroids[0][0] + centroids[0][1]) * 10000)
P2 = int((centroids[1][0] + centroids[1][1]) * 10000)
print(P1, P2)