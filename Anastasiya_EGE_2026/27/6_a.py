l=[[float(d.replace(',','.')) for d in x.split()] for x in open('6_a.txt')]
clusters=[[],[]]
for point in l:
    if point[0]<0:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids=[[],[]]
ind=0
for cluster in clusters:
    sm_rust=10**10
    for centroid in cluster:
        rast=0
        for point in cluster:
            rast+=((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)**0.5
        if rast<sm_rust:
            sm_rust=rast
            centroids[ind]=centroid
    ind+=1
Px=abs(int((centroids[0][0] + centroids[1][0])/2*10000))
Py=abs(int((centroids[0][1] + centroids[1][1])/2*10000))
print(Px,Py)
