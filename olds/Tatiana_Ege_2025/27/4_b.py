l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_b.txt')]
clusters = [[],[],[],[],[]]
for x in l:
    if x[1] > 2 and x[0] < -1:
        clusters[0].append(x)
    elif x[1] > 2:
        clusters[1].append(x)
    elif x[0] < -3:
        clusters[2].append(x)
    elif x[0] < 0:
        clusters[3].append(x)
    else:
        clusters[4].append(x)
corners = [[],[],[],[]]
del clusters[clusters.index(min(clusters, key=len))]
import math
ind = 0
for x in clusters:
    print(x)
    mx_sm_rast = 0
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += math.dist(y, z)
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            corners[ind] = y
    ind+=1
Tx = (corners[0][0]+corners[1][0]+corners[2][0]+corners[3][0])/4  *10000
Ty = (corners[0][1]+corners[1][1]+corners[2][1]+corners[3][1])/4*10000
print(int(Tx),int(Ty))