l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('8_a.txt')]
clusters=[[], [], []]
for point in l:
    if point[1]>0:
        clusters[0].append(point)
    elif point[0]>2:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
#print(len(clusters[0]), len(clusters[1]), len(clusters[2]))
del clusters[2]
centroids=[[], []]
ind=0
for cluster in clusters:
    mn_sm_rast=0
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
        if sm_rast>mn_sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
Px=int(((centroids[0][0]+centroids[1][0])/2)*10_000)
Py=int(((centroids[0][1]+centroids[1][1])/2)*10_000)
print(Px, Py)