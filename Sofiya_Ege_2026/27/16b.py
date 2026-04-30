import math
l=[[float(d.replace(',','.'))for d in x.split()]for x in open('16b.txt')]
clusters=[[],[],[]]
for point in l:
    if 10 <= point[1] <= 30:
        if point[1]<19:
            clusters[0].append(point)
        elif point[0]>19:
            clusters[1].append(point)
        else:
            clusters[2].append(point)
print(len(clusters[0]),len(clusters[1]),len(clusters[2]))
centroids=[[],[],[]]
ind=0
for cluster in clusters:
    mx_rast = 0
    for point1 in cluster:
        for point2 in cluster:
            if math.dist(point1, point2) > mx_rast:
                centroids[ind] = [point1,point2]
                mx_rast = math.dist(point1, point2)
    ind+=1
Q1 = int((math.dist(centroids[1][0], centroids[1][1])) * 10000)
mx_rast = 0
for p1 in centroids[0] + centroids[1] + centroids[2]:
    for p2 in centroids[0] + centroids[1] + centroids[2]:
        mx_rast = max(mx_rast, math.dist(p1, p2))
print(Q1, int(mx_rast * 10000))
#print(int(min(centroids[0][0][0] + centroids[0][1][0], centroids[1][0][0] + centroids[1][1][0]) * 10000), int(max(centroids[0][0][1] + centroids[0][1][1], centroids[1][0][1] + centroids[1][1][1]) * 10000))