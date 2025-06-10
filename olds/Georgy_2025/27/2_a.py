l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], [], []]
for x in l:
    if 1 <= x[1] <= 7 and x[0] > -1:
        clusters[0].append(x)
    elif x[1] <= 0 and x[0] < 0:
        clusters[1].append(x)
    elif x[0] > 0.5 and -6 < x[1] < 0:
        clusters[2].append(x)
ind = 0
centroids = [[], [], []]
for x in clusters:
    mx_sm_rast = 0
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(centroids)
print(Px, Py)