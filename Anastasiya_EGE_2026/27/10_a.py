l=[[float(d.replace(',','.')) for d in x.split()] for x in open('10_a.txt')]
clusters=[[],[]]
for point in l:
    if point[1]>5:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids= [[],[]]
anticentroids = [[], []]
ind=0
for cluster in clusters:
    mn_sm_rast=10**10
    mx_sm_rast=0
    for centroid in cluster:
        rast=0
        for point in cluster:
            rast+=((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)**0.5
        if rast<mn_sm_rast:
            mn_sm_rast=rast
            centroids[ind]=centroid
        if rast>mx_sm_rast:
            mx_sm_rast=rast
            anticentroids[ind]=centroid
    ind+=1
Px=abs(int((centroids[0][0] + centroids[1][0])/2*10000))
Sy=abs(int((anticentroids[0][1] + anticentroids[1][1])/2*10000))
print(Px, Sy)