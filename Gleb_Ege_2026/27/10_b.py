import math
l = [[d for d in x.split()] for x in open('10_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
clusters = [[], [], []]
for point in l:
    if point[1] > 22:
        clusters[0].append(point)
    elif point[0] > 20:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(point[:2], centroid[:2])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
ct = 0
ct1 = 0
ct2 = 0
for r in clusters[0]:
    if r[2][0] == 'L':
        ct += 1
print(ct)
for t in clusters[1]:
    if t[2][0] == 'L':
        ct1 += 1
print(ct1)
for u in clusters[2]:
    if u[2][0] == 'L':
        ct2 += 1
print(ct2)

sin1 = []
sin2 = []
sin3 = []
for s in clusters[0]:
    if s[2][0] == 'L':
        sin1.append(s)
for p in clusters[1]:
    if p[2][0] == 'L':
        sin2.append(p)
for d in clusters[2]:
    if d[2][0] == 'L':
        sin3.append(d)
e = []
for i in sin1:
    for a in sin2:
        e.append(int(math.dist(i[:-1], a[:-1]) * 10000))
for i in sin2:
    for a in sin3:
        e.append(int(math.dist(i[:-1], a[:-1]) * 10000))
for i in sin1:
    for a in sin3:
        e.append(int(math.dist(i[:-1], a[:-1]) * 10000))
print(int(math.dist(centroids[0][:-1], centroids[1][:-1]) * 10000), max(e))