from math import *
dots = [[float(d.replace(',', '.')) for d in x.split()] for x in open('10_a.txt')]
cl = []
while dots:
    clast = [dots.pop()]
    for p in clast:
        sosed = [p1 for p1 in dots if dist(p, p1) < 0.7]
        clast.extend(sosed)
        for p1 in sosed:
            dots.remove(p1)
    cl.append(clast)
print([len(x) for x in cl])
cl.pop(1)
centroids = [[], [], [], []]
ind = 0
for cluster in cl:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += dist(centroid, point)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0]) / 4 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000)
print(Px, Py)