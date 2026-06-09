from math import* #BBB
l = [[[float(d.replace(',','.')) for d in x.split()[:-1]],x.split()[-1]] for x in open('13_b.txt')]
clusters = [[],[],[]]
for p in l:
    if p[0][1] > 23:
        clusters[0].append(p)
    elif p[0][0] > 20:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[],[],[]]
ind = 0
for cluster in clusters:
    mx_sm_rast = 10**10
    for centroid in cluster:
        mx_rast = 0
        for p in cluster:
            mx_rast += dist(centroid[0],p[0])
        if mx_rast < mx_sm_rast:
            mx_sm_rast = mx_rast
            centroids[ind] = centroid
    ind+=1
ind = 0
mn_rast = []
sr_rast = []
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if (p1[1] != 'VII' and p2[1] != 'VII'):
            if (int(p1[1][1]) >= 8 and int(p2[1][1]) >= 8):
                mn_rast.append(dist(p1[0],p2[0]))
for p1 in clusters[1]:
    for p2 in clusters[2]:
        if (p1[1] != 'VII' and p2[1] != 'VII'):
            if (int(p1[1][1]) >= 8 and int(p2[1][1]) >= 8):
                mn_rast.append(dist(p1[0],p2[0]))
for p1 in clusters[0]:
    for p2 in clusters[2]:
        if (p1[1] != 'VII' and p2[1] != 'VII'):
            if(int(p1[1][1]) >= 8 and int(p2[1][1]) >= 8):
                mn_rast.append(dist(p1[0],p2[0]))
for x in range(3):
    for p1 in clusters[x]:
        for p2 in clusters[x]:
            if (p1[1] != 'VII' and p2[1] != 'VII'):
                if p1 != p2 and (int(p1[1][1]) >= 8 and int(p2[1][1]) >= 8):
                    sr_rast.append(dist(p1[0],p2[0]))
print(int(min(mn_rast)*10000),int((sum(sr_rast)/len(sr_rast))*10000))