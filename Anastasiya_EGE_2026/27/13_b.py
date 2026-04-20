import math

l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('13_b.txt')]
clusters = [[], [], []]
for point in l:
    if point[1] > 22:
        clusters[0].append(point)
    elif point[0] > 24:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    sm_rust = 10 ** 10
    for centroid in cluster:
        rast = 0
        for point in cluster:
            rast += ((centroid[0] - point[0]) ** 2 + (centroid[1] - point[1]) ** 2) ** 0.5
        if rast < sm_rust:
            sm_rust = rast
            centroids[ind] = centroid
    ind += 1
ctB1 = 0
for p in clusters[2]:
    if math.dist(p, centroids[2]) <= 1.2:
        ctB1 += 1
mn_rast = []
for p in clusters[0]:
    if p != centroids[0]:
        mn_rast.append(math.dist(p, centroids[0]))
print(ctB1 - 1, int(min(mn_rast) * 10000))