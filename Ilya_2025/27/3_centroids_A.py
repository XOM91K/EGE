l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_centroids_A.txt')]
#k_means
clusters = [[], []]
for x in l:
    if x[0] < 1:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
centroids = [[], []]
ind = 0
for x in clusters:
    print(x)
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            dist = ((z[0] - y[0]) ** 2 + (z[1] - y[1]) ** 2) ** 0.5
            sm_rast += dist
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
Px = int((centroids[0][0] + centroids[1][0]) / 2 * 10000)
Py = int((centroids[0][1] + centroids[1][1]) / 2 * 10000)
print(Px, Py)