import math
l=[[float(d.replace(',','.'))for d in x.split()]for x in open('16a.txt')]
clusters=[[],[]]
for point in l:
    if point[1]>10:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids=[[],[]]
ind=0
for cluster in clusters:
    mx_rast = 0
    for point1 in cluster:
        for point2 in cluster:
            if math.dist(point1, point2) > mx_rast:
                centroids[ind] = [point1, point2]
    ind+=1
print(int(min(centroids[0][0][0] + centroids[0][1][0], centroids[1][0][0] + centroids[1][1][0]) * 10000))