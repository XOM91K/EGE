l=[[d for d in x.split()]for x in open('19_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',', '.')), float(l[x][1].replace(',', '.')), l[x][2]]
clusters=[[],[],[]]
for point in l:
    if point[1]>22:
        clusters[0].append(point)
    elif point[1]<15:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
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
d=[]
for p in clusters[0]:
    if p!=centroids[0]:
        if p[-1][0]=='L' and p[-1][-1]=='V':
          d.append(dist(centroids[0][:-1],p[:-1]))
for p in clusters[1]:
    if p!=centroids[1]:
        if p[-1][0]=='L' and p[-1][-1]=='V':
          d.append(dist(centroids[1][:-1],p[:-1]))
for p in clusters[2]:
    if p!=centroids[2]:
        if p[-1][0]=='L' and p[-1][-1]=='V':
          d.append(dist(centroids[2][:-1],p[:-1]))
print(int(min(d)*10000),int(max(d)*10000))