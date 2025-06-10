l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('3_b.txt')]
clusters = [[], [], [], [], []]
for x in l:
    if x[0] < 7 and x[1] < 5:
        clusters[0].append(x)
    elif x[0] < 8 and 5 < x[1] < 10:
        clusters[1].append(x)
    elif 10 < x[1] < 13:
        clusters[2].append(x)
    elif x[1] > 13:
        clusters[3].append(x)
    elif x[0] > 12:
        clusters[4].append(x)

centroids = [clusters[0][0], clusters[1][0], clusters[2][0], clusters[3][0], clusters[4][0]]
ind = -1
for x in clusters:
    ind += 1
    mx_sum_rast = 10**10
    for y in x:
        sum_rast = 0
        for z in x:
            distance = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
            sum_rast += distance
        if sum_rast < mx_sum_rast:
            mx_sum_rast = sum_rast
            centroids[ind] = y

Px = int(((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5) * 10000)
Py = int(((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5) * 10000)

print(Px, Py)