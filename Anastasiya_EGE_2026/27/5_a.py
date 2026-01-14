l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('5_a.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] > 0 and point[0] < 1:
        clusters[0].append(point)
    elif point[0] > 1:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    srX = 0
    srY = 0
    for point in cluster:
        srX += point[0]
        srY += point[1]
    srX = srX / len(cluster)
    srY = srY / len(cluster)
    centroids[ind] = [srX, srY]
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)