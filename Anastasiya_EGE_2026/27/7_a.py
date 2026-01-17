import math
l=[[float(d.replace(',','.')) for d in x.split()] for x in open('7_a.txt')]
clusters=[[],[],[]]
for point in l:
    if point[1]<1 and point[0]<0:
        clusters[0].append(point)
    elif point[0]>0.5 and -6 <= point[1] <= 0:
        clusters[1].append(point)
    elif 0 <= point[1] <= 6.3 and -1<point[0]<7:
        clusters[2].append(point)
centroids=[[],[],[]]
ind=0
for cluster in clusters:
    print(cluster)
    mx_sm_rast=0
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
           # print(point, centroid)
            sm_rast+=math.dist(point,centroid)
        if sm_rast>mx_sm_rast:
            mx_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
Tx=abs(int((centroids[0][0]+centroids[1][0]+centroids[2][0])/3*10000))
Ty=abs(int((centroids[0][1]+centroids[1][1]+centroids[2][1])/3*10000))
print(Tx,Ty)