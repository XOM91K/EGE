l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('5_a.txt')]
clusters=[[], [], []]
for point in l:
    if point[1] > 5.5:
        clusters[0].append(point)
    elif point[1] > 3:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
ind=0
radiuses = [0, 0, 0]
centroids=[[], [], []]
for cluster in clusters:
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast =0
        mx_rast = 0
        for point in cluster:
            sm_rast+=((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
            mx_rast = max(mx_rast, ((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5)
        if sm_rast<mn_sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
            radiuses[ind] = mx_rast

    ind+=1
minimal=int(min(radiuses)*10000)
maximal=int(max(radiuses)*10000)
print(minimal, maximal)