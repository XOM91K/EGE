import math
a = [[float(i.replace(',','.')) for i in x.split()]for x in open('7.txt')]
clusters =[[],[]]
for i in a:
    if i[1]>20:
        clusters[0].append(i)
    else:
        clusters[1].append(i)
centroids = [[],[]]
ind=0
for x in clusters:
    min_rast = 10**10
    for y in x:
        rast =0
        for z in x:
            rast +=math.dist(y,z)
        if min_rast>rast:
            min_rast =rast
            centroids[ind]= y
    ind+=1
Px = int((centroids[0][0]+centroids[1][0])/2*10_000)
Py = int((centroids[0][1]+ centroids[1][1])/2*10_000)
print(Px, Py)