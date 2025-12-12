l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_a.txt')]
clusters = [[], []]
for x in l:
    if x[1] > 0:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
centroids = [[], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10**10
    for y in x:
        rast = 0
        for z in x:
            rast += ((y[0] - z[0])**2 + (y[1] - z[1])**2)**0.5
        if rast < mn_sm_rast:
            mn_sm_rast = rast
            centroids[ind] = y
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0])/2 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1])/2 * 10000))
print(Px, Py)