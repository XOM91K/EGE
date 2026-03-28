l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], [], [], []]
for p in l:
    if p[1] > 14:
        clusters[0].append(p)
    elif p[1] < 4:
        clusters[1].append(p)
    elif p[0] > 16:
        clusters[2].append(p)
    else:
        clusters[3].append(p)
centroids = [[], [], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += ((p1[0] - p2[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000)
print(Px, Py)