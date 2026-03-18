from turtle import *
from random import *
l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('20.txt')]
clusters=[[],[]]
for point in l:
    if point[1]>point[0]-4 and not(1 <= point[0] <= 3 and 1.9 <= point[1] <= 3) and not(7 <= point[0] <= 8 and -2 <= point[1] <= -1):
        clusters[0].append(point)
    elif not(1 <= point[0] <= 3 and 1.9 <= point[1] <= 3) and not(7 <= point[0] <= 8 and -2 <= point[1] <= -1):
        clusters[1].append(point)
for x in clusters:
    print(len(x))
centroids=[[],[]]
ind=0
for cluster in clusters:
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
        if sm_rast<mn_sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
Px=abs(int(((centroids[0][0]+centroids[1][0])/2)*100_000))
Py=abs(int(((centroids[0][1]+centroids[1][1])/2)*100_000))
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