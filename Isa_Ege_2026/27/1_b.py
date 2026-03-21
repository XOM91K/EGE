l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1_b.txt')]
clusters = [[], [], []]
for p in l:
    if p[1] > 7:
        clusters[0].append(p)
    elif p[1] > 4:
        clusters[1].append(p)
    else:
        clusters[2].append(p)

centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(Px, Py)