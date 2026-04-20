import math
l=[[float(d.replace(',','.')) for d in x.split()] for x in open('13_a.txt')]
clusters=[[],[]]
for point in l:
    if point[1]>15:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids=[[],[]]
ind=0
for cluster in clusters:
    print(len(cluster))
    sm_rust=10**10
    for centroid in cluster:
        rast=0
        for point in cluster:
            rast+=((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)**0.5
        if rast<sm_rust:
            sm_rust=rast
            centroids[ind]=centroid
    ind+=1
A1=344
A2=int((math.dist(centroids[0], [1.0, 1.5]) + math.dist(centroids[1], [1.0, 1.5])) * 10000)
print(A1, A2)