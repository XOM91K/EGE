# import math
# l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('4_a.txt')]
# clusters=[[], []]
# for point in l:
#     if point[0]<40:
#         clusters[0].append(point)
#     else:
#         clusters[1].append(point)
# ind=0
# centroids=[[], []]
# for cluster in clusters:
#     print(len(cluster))
#     mn_sm_rast=10**10
#     for centroid in cluster:
#         sm_rast=0
#         for point in cluster:
#             sm_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
#         if sm_rast<mn_sm_rast:
#             mn_sm_rast=sm_rast
#             centroids[ind]=centroid
#     ind+=1
#
# Px=abs(int((centroids[0][0]+centroids[0][1])*10_000))
# Py=abs(int((centroids[1][0]+centroids[1][1])*10_000))
# print(Px, Py)

import math
l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('4_b.txt')]
clusters=[[], [], []]
for point in l:
    if point[1]<32 and point[0] > 11:
        clusters[0].append(point)
    elif point[1]>42 and point[0] > 11:
        clusters[1].append(point)
    elif point[0] > 11:
        clusters[2].append(point)
ind=0
centroids=[[], [], []]
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=math.dist(centroid, point)
        if sm_rast<mn_sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1

Px=(int((centroids[1][0])*10_000))
Py=(int((centroids[0][1])*10_000))
print(Px, Py)
# l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('2_b')]
# clusters=[[], [], []]
# for point in clusters:
#     if point[1]<32:
#         clusters[0].append(point)
#     elif point[1]>42:
#         clusters[2].append(point)
#     else:
#         clusters[1].append(point)
# ind=[]
# centroids=[[], [], []]
# for cluster in clusters:
#     mn_sm_rast=10**10
#     for centroid in cluster:
#         sm_rast=0
#         for point in cluster:
#             sm_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
#         if sm_rast<mn_sm_rast:
#             mn_sm_rast=sm_rast
#             centroids[ind]=centroid
#     ind+=1
# Px=int(((centroids[0][0]+centroids[1][0])+centroids[2][0])/3)*10_000)
# Py=int(((centroids[0][0]+centroids[1][1]+centroids[2][1])/3)*10_000)
# print(Px, Py)