import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('14_a.txt')]
clusters = [[], []]
for p in l:
    if p[1] > 10:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    sm_rust=10**10
    for centroid in cluster:
        rast=0
        for point in cluster:
            rast+=((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)**0.5
        if rast<sm_rust:
            sm_rust=rast
            centroids[ind]=centroid
    ind+=1
Px = int(min(math.dist(centroids[0], [5.5, 9.1]), math.dist(centroids[1], [5.5, 9.1])) * 10000)
new_tchk = [(centroids[0][0] + centroids[1][0]) / 2, (centroids[0][1] + centroids[1][1]) / 2]
Py = int(math.dist([5.5, 9.1], new_tchk) * 10000)
print(Px, Py)