l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_b.txt')]
clusters = [[], [], []]
for x in l:
    if x[1] < 0:
        clusters[0].append(x)
    elif x[0] > -6:
        clusters[1].append(x)
    elif x[0] < -6:
        clusters[2].append(x)
centroids = [[], [], []]
ind = 0
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
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)