l = [[float(d.replace(',','.')) for d in x.split()] for x in open('5.txt')]
clusters = [[], [], []]
for x in l:
    if x[0] < 0 and x[1] < 0.5:
        clusters[0].append(x)
    elif x[0] > 0.5 and -6 <= x[1] <= 0:
        clusters[1].append(x)
    elif x[0] > -1 and 0.2 <= x[1] <= 7:
        clusters[2].append(x)
centroids = [[], [], []]
ind = 0
for x in clusters:
    mx_sum_rast = 0
    for y in x:
        rast = 0
        for z in x:
            rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if rast > mx_sum_rast:
            mx_sum_rast = rast
            centroids[ind] = y
    ind += 1
Tx = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Ty = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(Tx, Ty)