l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], [], []]
for x in l:
    if x[0] < 0 and x[1] < 0.1:
        clusters[0].append(x)
    elif 0.5 <= x[0] <= 4 and -6 <= x[1] <= 0:
        clusters[1].append(x)
    elif -1 <= x[0] <= 2 and 1 <= x[1] <= 7:
        clusters[2].append(x)
centroids = [[], [], []]
ind = 0
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
print(centroids)
Tx = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Ty = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(Tx, Ty)