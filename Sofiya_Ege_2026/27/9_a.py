l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('9_a.txt')]
clusters=[[], [], []]
for point in l:
    if point[0]<0 and point[1]<1:
        clusters[0].append(point)
    elif point[0]>0.5 and -5 <= point[1] <= 0:
        clusters[1].append(point)
    elif -1 <= point[0] <= 2 and 0 <= point[1] <= 6:
        clusters[2].append(point)
centroids=[[],[],[]]
ind=0
for cluster in clusters:
    print(cluster)
    mx_sm_rast=0
    for centroid in cluster:
        mx_rast=0
        for point in cluster:
            mx_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
        if mx_sm_rast<mx_rast:
            mx_sm_rast=mx_rast
            centroids[ind]=centroid
    ind+=1
Px=abs(int(((centroids[0][0]+centroids[1][0]+centroids[2][0]) / 3*10_000)))
Py=abs(int(((centroids[0][1]+centroids[1][1]+centroids[2][1]) / 3*10_000)))
print(Px, Py)