from turtle import *
from random import *
screensize(1920, 1080)
l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('11_a.txt')]
clusters=[[], [], []]
for point in l:
    if point[1]<0:
        clusters[0].append(point)
    elif point[1] > (8 / 9) * point[0] - (112 / 9):
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids=[[],[],[]]
ind=0
for cluster in clusters:
    print(cluster)
    mn_sm_rast=10 ** 10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
tracer(0)
up()
for cluster in clusters:
    color=random(), random(), random()
    for x, y in cluster:
        goto(x*30 - 1000, y*30 - 250)
        dot(5, color)
update()
done()
Px=abs(int(((centroids[0][0]+centroids[1][0]+centroids[2][0]) / 3*10_000)))
Py=abs(int(((centroids[0][1]+centroids[1][1]+centroids[2][1]) / 3*10_000)))
print(Px, Py)
# 280340      52489