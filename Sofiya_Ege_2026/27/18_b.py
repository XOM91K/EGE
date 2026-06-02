l= [[d for d in x.split()]for x in open('18_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',', '.')), float(l[x][1].replace(',', '.')), l[x][2]]
clusters = [[], [],[]]
for point in l:
    if point[0]>22:
        clusters[0].append(point)
    elif point[1]>22:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
d=0
e=0
f=0
for a in clusters[0]:
    if a[-1][0]=='L':
        d+=1
for b in clusters[1]:
    if b[-1][0]=='L':
        e+=1
for c in clusters[2]:
    if c[-1][0]=='L':
        f+=1
print(d,e,f)
centroids=[[],[],[]]
ind=0
from math import *
for cluster in clusters:
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=dist(centroid[:-1],point[:-1])
        if mn_sm_rast>sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
print(centroids)
b1=dist(centroids[0][:-1],centroids[1][:-1])
d=[]
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if p1[-1][0]=='L' and p2[-1][0]=='L':
            d.append(dist(p1[:-1],p2[:-1]))
for p1 in clusters[0]:
    for p2 in clusters[2]:
        if p1[-1][0]=='L' and p2[-1][0]=='L':
            d.append(dist(p1[:-1],p2[:-1]))
for p1 in clusters[2]:
    for p2 in clusters[1]:
        if p1[-1][0]=='L' and p2[-1][0]=='L':
            d.append(dist(p1[:-1],p2[:-1]))
print(d)
print(int((b1)*10_000),int(max(d)*10_000))
