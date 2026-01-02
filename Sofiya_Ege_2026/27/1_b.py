l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] < 3:
        clusters[0].append(point)
    elif point[1] > 7:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for star in cluster:
            sm_rast += ((centroid[0] - star[0]) ** 2 + (centroid[1] - star[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
print(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
print(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
# 37522 51277