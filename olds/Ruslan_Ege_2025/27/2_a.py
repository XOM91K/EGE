l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], []]
for x in l:
    if x[1] < 6:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
centroids = [[], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            rast = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
            sm_rast += rast
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
print(centroids)
px = int((centroids[0][0] + centroids[1][0])/ 2*10000)
py = int((centroids[0][1] + centroids[1][1])/2*10000)
print(px, py)