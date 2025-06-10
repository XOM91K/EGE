a = [[float(i.replace(',','.')) for i in x.split()] for x in open('8.txt') ]
import math
clusters =[[],[],[]]
for i in range(len(a)):
    if a[i][1]<0 and a[i][0]<1:
        clusters[0].append(a[i])
    elif  a[i][1]>0 and a[i][0]<1:
        clusters[1].append(a[i])
    else:
        clusters[2].append(a[i])
centroids =[[],[],[]]
ind =0
for x in clusters:
    sr_x = []
    sr_y = []
    for y in x:
        sr_x.append(y[0])
        sr_y.append(y[1])
    sr_x = sum(sr_x) / len(sr_x)
    sr_y = sum(sr_y) / len(sr_y)
    centroids[ind] = [sr_x, sr_y]
    ind += 1
Px = int((centroids[0][0]+ centroids[1][0]+ centroids[2][0])/3*10_000)
Py = int((centroids[0][1]+ centroids[1][1]+ centroids[2][1])/3*10_000)
print(abs(Px), abs(Py))