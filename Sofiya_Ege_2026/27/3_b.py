import math
l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('3_b.txt')]
clusters=[[], [], [], [], []]
for point in l:
    if point[0]>12:
        clusters[0].append(point)
    elif 4<point[0]<7 and point[1]<5:
        clusters[1].append(point)
    elif 6<point[1]<9:
        clusters[2].append(point)
    elif 10<point[1]<13:
        clusters[3].append(point)
    else:
        clusters[4].append(point)
ind=0
centroids=[[], [], [], [], []]
for cluster in clusters:
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=math.dist(point, centroid)
        if sm_rast<mn_sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
Px=int(((centroids[0][0]+centroids[1][0]+centroids[2][0]+centroids[3][0]+centroids[4][0])/5)*10_000)
Py=int(((centroids[0][1]+centroids[1][1]+centroids[2][1]+centroids[3][1]+centroids[4][1])/5)*10_000)
print(Px, Py)