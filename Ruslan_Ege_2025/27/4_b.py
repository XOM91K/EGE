l = [[float(d.replace(',','.')) for d in g.split()] for g in open('4_b.txt')]
clusters = [[], [], []]
for x in l:
    if x[0] < 1.3:
        clusters[0].append(x)
    elif x[0] < 5:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
centroids = [[], [], []]
mn_rast = 10 ** 10
for x in clusters[0]:
    for y in clusters[1]:
        for z in clusters[2]:
            rast1 = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
            rast2 = ((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2) ** 0.5
            rast3 = ((z[0] - y[0]) ** 2 + (z[1] - y[1]) ** 2) ** 0.5
            if rast1 + rast2 + rast3 < mn_rast:
                mn_rast = rast1 + rast2 + rast3
                centroids[0] = x
                centroids[1] = y
                centroids[2] = z
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(Px, Py)