l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1_b.txt')]
clusters = [[], [], []]
for x in l:
    if -1 <= x[0] <= 3 and -1 <= x[1] <= 4:
        clusters[0].append(x)
    elif 5 <= x[0] <= 8 and 2 <= x[1] <= 8:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
centroids = [[], [], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            rast = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
            sm_rast += rast
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(Px, Py)