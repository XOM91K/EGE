l=[[float(d.replace(',','.'))for d in x.split()]for x in open('14_b.txt')]
clusters=[[],[],[]]
for point in l:
    if point[0]>24:
        clusters[0].append(point)
    elif point[1]>22:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
print(len(clusters[0]),len(clusters[1]),len(clusters[2]))
centroids=[[],[],[]]
ind=0
from math import *
for cluster in clusters:
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=dist(centroid,point)
        if mn_sm_rast>sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
ct1=0
for p in clusters[2]:
    if dist(centroids[2],p)<=1.2:
        ct1+=1
B2=sorted([dist(centroids[1], p) for p in clusters[1]])
print(ct1 - 1,int(B2[1]*10_000))
