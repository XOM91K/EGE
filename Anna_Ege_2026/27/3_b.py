l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_b.txt')]
clusters = [[], [], []]
for x in l:
    if 21 < x[1] < 28:
        clusters[0].append(x)
    elif 4 <= x[1] <= 12:
        clusters[1].append(x)
    elif 16 <= x[1] <= 21:
        clusters[2].append(x)
centroids = [[], []]
ind = 0
del clusters[-1]
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        rast = 0
        for z in x:
            rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if rast < mn_sm_rast:
            mn_sm_rast = rast
            centroids[ind] = y
    ind += 1
Px = int(abs(centroids[0][0] - centroids[1][0]) * 10000)
Py = int(abs(centroids[0][1] - centroids[1][1]) * 10000)
print(Px, Py)