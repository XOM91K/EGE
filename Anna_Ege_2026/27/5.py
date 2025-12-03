l = [[float(d.replace(',','.')) for d in x.split()] for x in open('5.txt')]
clusters = [[], [], []]
for x in l:
    if x[1] > 6:
        clusters[0].append(x)
    elif x[1] < 2:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
clusters.remove(min(clusters, key=len))
# for x in clusters:
#     print(x)
centroids = [[], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            centroids[ind] = y
            mn_sm_rast = sm_rast
    ind += 1
print(centroids)
print((centroids[0][0] + centroids[1][0]) / 2 * 10000)
print((centroids[0][1] + centroids[1][1]) / 2 * 10000)