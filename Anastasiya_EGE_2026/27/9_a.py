import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('9_a.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] < 2:
        clusters[0].append(point)
    elif point[1] > 5.5:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
rads = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        rad = 0
        rast = 0
        for point in cluster:
            rast += ((centroid[0] - point[0])**2 + (centroid[1] - point[1])**2)**0.5
            rad = max(rad, ((centroid[0] - point[0])**2 + (centroid[1] - point[1])**2)**0.5)
        if rast < mn_sm_rast:
            mn_sm_rast = rast
            centroids[ind] = centroid
            rads[ind] = rad
    ind += 1
Px = int(min(rads) * 10000)
Py = int(max(rads) * 10000)
print(Px, Py)