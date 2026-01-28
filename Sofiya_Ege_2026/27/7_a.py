import math
l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('7_a.txt')]
clusters=[[] ,[]]
for point in l:
    if point[1]<5:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
diags = [[], []]
ind=0
for cluster in clusters:
    mx_rast = 0
    for point1 in cluster:
        for point2 in cluster:
            if math.dist(point1, point2) > mx_rast:
                mx_rast = math.dist(point1, point2)
                diags[ind] = [point1, point2]
    ind+=1
Px = int((diags[0][0][0] + diags[0][1][0] + diags[1][0][0] + diags[1][1][0]) / 4 * 10000)
Py = int((diags[0][0][1] + diags[0][1][1] + diags[1][0][1] + diags[1][1][1]) / 4 * 10000)
print(Px, Py)