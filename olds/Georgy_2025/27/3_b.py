l = [[float(d.replace(',','.')) for d in x.split()] for x in open("3_b.txt")]
cluster = [[],[],[],[],[]]
for x in l:
    if x[0] < 7:
        cluster[0].append(x)
    elif 7 < x[0] < 15:
        cluster[1].append(x)
    elif 15 < x[0] < 24:
        cluster[2].append(x)
    elif 24 < x[0] < 28:
        cluster[3].append(x)
    else:
        cluster[4].append(x)
centroid = [[],[],[],[],[]]
ind = 0
for x in cluster:
    mn_sm_rast = 10**10
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((y[0] - z[0])**2 + (y[1] - z[1])**2)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroid[ind] = y
    ind += 1
Px = int((centroid[0][0] + centroid[1][0] + centroid[2][0] + centroid[3][0] + centroid[4][0])/5*10000)
Py = int((centroid[0][1] + centroid[1][1] + centroid[2][1] + centroid[3][1] + centroid[4][1])/5*10000)
print(Px,Py)