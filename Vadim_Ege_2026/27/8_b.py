from turtle import *
from random import random
f = [[float(d.replace(',', '.')) for d in x.split()] for x in open('8_b.txt')]
clusters = [[], [], [], [], []]
line1 = [x - 1 for x in range(0, 15)]
line2 = [-1 * x + 1 for x in range(0, 15)]
for p in f:
    if p[0] < -2 and p[1] < 0:
        clusters[0].append(p)
    elif p[1] > 0 and p[0] < -2:
        clusters[1].append(p)
    elif p[1] > line1[int(p[0])]:
        clusters[2].append(p)
    elif p[1] < line2[int(p[0])]:
        clusters[3].append(p)
    else:
        clusters[4].append(p)

centroids = [[], [], [], [], []]
ind = 0
for cluster in clusters:
    centroid = []
    x = 0
    y = 0
    for point in cluster:
        x += point[0]
        y += point[1]
    centroid.append(x / len(cluster))
    centroid.append(y / len(cluster))
    centroids[ind] = centroid
    ind += 1
Px = (centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000
Py = (centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5 * 10000
print(Px, Py)
tracer(0)
up()
for cluster in clusters:
    color=random(), random(), random()
    for x, y in cluster:
        goto(x*30, y*30)
        dot(5, color)
update()
done()