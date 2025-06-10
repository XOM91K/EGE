l = [[float(d) for d in x.split()] for x in open('9_b.txt')]
clusters = [[], [], []]
for x in l:
    if x[0] < 1:
        clusters[0].append(x)
    elif x[0] < 3:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
clusters = sorted(clusters, key=len)[1:]
centroids = [[], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
radius = [0, 0]
ind = 0
for x in clusters:
    for y in x:
        radius[ind] = max(radius[ind], (((y[0] - centroids[ind][0]) ** 2 + (y[1] - centroids[ind][1]) ** 2)) ** 0.5)
    ind += 1
print(centroids)
print(int(sum(radius) / len(radius) * 10000))