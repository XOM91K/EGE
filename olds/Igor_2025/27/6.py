import math
l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('6.txt')]
clusters_coords = [[3, 7, 0, 4], [6, 10, 10, 14], [21, 25, 4.5, 8], [24, 28, 0, 4.4], [29, 32, 0, 4]]
clusters = [[]] * len(clusters_coords)
centroids = [[]] * len(clusters_coords)
for x in l:
    for y in range(len(clusters_coords)):
        if clusters_coords[y][0] <= x[0] <= clusters_coords[y][1] and clusters_coords[y][2] <= x[1] <= clusters_coords[y][3]:
            clusters[y].append(x)
for item in range(len(clusters)):
    centroids[item].append(clusters[item][0])
    centroids[item].append(10 ** 10)
    for point in range(len(clusters[item])):
        sm = 0
        for x in range(len(clusters[item])):
            if point != x:
                sm += math.sqrt((clusters[item][point][0] - clusters[item][x][0]) ** 2 + (clusters[item][point][1] - clusters[item][x][1]) ** 2)
        if sm < centroids[item][1]:
            centroids[item][1] = sm
            centroids[item][0] = clusters[item][point]
Px = int(sum([x[0][0] for x in centroids]) / len(centroids) * 10000)
Py = int(sum([x[0][1] for x in centroids]) / len(centroids) * 10000)
print(Px, Py)