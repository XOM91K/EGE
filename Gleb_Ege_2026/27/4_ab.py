l = [[float(d.replace(',','.')) for d in x.split()]for x in open('4_a.txt')]
clusters = [[], [], []]
for point in l:
    if point[0] > 1:
        clusters[0].append(point)
    elif point[1] < 0:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    smX = 0
    smY = 0
    for point in cluster:
        smX += point[0]
        smY += point[1]
    centroids[ind] = [smX / len(cluster), smY / len(cluster)]
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)