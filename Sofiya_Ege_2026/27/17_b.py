l = [[d for d in x.split()] for x in open('17_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
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
mn_rast=[]
print(centroids)
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if p1 != p2 and p1[2][1] in '89' and p2[2][1] in '89':
            mn_rast.append(dist(p1[:-1], p2[:-1]))
for p1 in clusters[1]:
    for p2 in clusters[2]:
        if p1 != p2 and p1[2][1] in '89' and p2[2][1] in '89':
            mn_rast.append(dist(p1[:-1], p2[:-1]))
for p1 in clusters[0]:
    for p2 in clusters[2]:
        if p1 != p2 and p1[2][1] in '89' and p2[2][1] in '89':
            mn_rast.append(dist(p1[:-1], p2[:-1]))
# ----------------
sr_rast = []
for p1 in clusters[0]:
    for p2 in clusters[0]:
        if p1 != p2 and p1[2][1] in '89' and p2[2][1] in '89':
            sr_rast.append(dist(p1[:-1], p2[:-1]))
for p1 in clusters[1]:
    for p2 in clusters[1]:
        if p1 != p2 and p1[2][1] in '89' and p2[2][1] in '89':
            sr_rast.append(dist(p1[:-1], p2[:-1]))
for p1 in clusters[2]:
    for p2 in clusters[2]:
        if p1 != p2 and p1[2][1] in '89' and p2[2][1] in '89':
            sr_rast.append(dist(p1[:-1], p2[:-1]))
sr_rast = sum(sr_rast) / len(sr_rast)
print(int(min(mn_rast) * 10000), int(sr_rast * 10000))
# for cluster in clusters:
#     ct = 0
#     for p1 in cluster:
#         if :
#             ct += 1
#         for p2 in cluster:
#             if :
#                 mn_rast.append(dist(p1[:-1], p2[:-1]))