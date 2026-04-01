import math
l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('8_b.txt')]
clusters = [[], [], []]
for p in l:
    if p[1] > 34:
        clusters[0].append(p)
    elif 34 > p[1] > 28:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(point, centroid)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
p = [1.7, 2.3]
Q1 = int(min(math.dist(p, centroids[2]), math.dist(p, centroids[1]), math.dist(p, centroids[0])) * 10000)
Q2 = int(max(math.dist(p, centroids[2]), math.dist(p, centroids[1]), math.dist(p, centroids[0])) * 10000)
print(Q1, Q2)