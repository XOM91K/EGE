l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('5.txt')]
clusters = [[], [], [], []]
for x in l:
    if x[1] > 14:
        clusters[0].append(x)
    elif x[0] <= 10 and x[1] < 14:
        clusters[1].append(x)
    elif 10 < x[0] < 15:
        clusters[2].append(x)
    else:
        clusters[3].append(x)

centroids = [[], [], [], []]
ind = -1
for x in clusters:
    ind += 1
    mx_sum_rast = 10**10
    for y in x:
        sum_rast = 0
        for z in x:
            d = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2)**0.5
            sum_rast += d
        if sum_rast < mx_sum_rast:
            mx_sum_rast = sum_rast
            centroids[ind] = y

Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000)

print(Px, Py)