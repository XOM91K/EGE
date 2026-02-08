l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_a.txt')]
clusters = [[],[]]
for points in l:
    if points[0]>40:
        clusters[0].append(points)
    else:
        clusters[1].append(points)
print(len(clusters[0]),len(clusters[1]))
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_rast = 10**10
    for centroid in cluster:
        rast = 0
        for point in cluster:
            rast += ((point[0]-centroid[0])**2+(point[1]-centroid[1])**2)**0.5
        if rast < mn_rast:
            rast = mn_rast
            centroids[ind] = centroid
    ind+=1
Px = int((centroids[0][0] + centroids[0][1]) * 10000)
Py = int((centroids[1][0] + centroids[1][1]) * 10000)
print(Py,Px)