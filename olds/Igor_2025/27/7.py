import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7.txt')]
clusters = [[], [], []]
centroids = []
for x in l:
    if -17 <= x[0] <= -9:
        clusters[0].append(x)
    elif -8.9 <= x[0] <= 0:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
for i in range(len(clusters)):
    centroid = [[], 10 ** 10]
    for x in clusters[i]:
        sm = 0
        for y in clusters[i]:
            d = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
            sm += d
        if sm < centroid[1]:
            centroid[1] = sm
            centroid[0] = x
    centroids.append(centroid[0])
print(centroids)
Px = abs((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3) * 10000
Py = abs((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3) * 10000
print(int(Px), int(Py))
