l = [[float(d.replace(',','.')) for d in g.split()] for g in open('4_a.txt')]
clusters = [[], []]
for x in l:
    if -2 <= x[0] <= 4:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
centroids = [[], []]
mn_rast = 10 ** 10
for x in clusters[0]:
    for y in clusters[1]:
        rast = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
        if rast < mn_rast:
            mn_rast = rast
            centroids[0] = x
            centroids[1] = y
Px = int((centroids[0][0] + centroids[1][0]) / 2 * 10000)
Py = int((centroids[0][1] + centroids[1][1]) / 2 * 10000)
print(Px, Py)