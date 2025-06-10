import math
a = [[float(i.replace(',','.')) for i in x.split()] for x in open('9_a.txt')]
clusters =[[],[],[],[]]
for i in range(len(a)):
    if a[i][0]<0:
        clusters[0].append(a[i])
    elif a[i][0]>0 and a[i][1]<0:
        clusters[1].append(a[i])
    elif a[i][0]>0 and a[i][1]>0 and a[i][1]<9:
        clusters[2].append(a[i])
    else:
        clusters[3].append(a[i])
for x in clusters:
    print(len(x))
centroids =[[],[],[],[]]
ind =0
for x in clusters:
    min_rast = 10 ** 10
    for y in x:
        rast =0
        for z in x:
            rast+=math.dist(y,z)
        if rast<min_rast:
            min_rast= rast
            centroids[ind]=y
    ind += 1
print(centroids)
Px = int(abs((centroids[0][0]+centroids[1][0]+centroids[2][0]+centroids[3][0])/4)*10000)
Py = int((centroids[0][1]+centroids[1][1]+centroids[2][1]+centroids[3][1])/4*10000)
print(abs(Px),abs(Py))