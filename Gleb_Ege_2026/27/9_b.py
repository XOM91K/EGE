import math
l = [[d for d in x.split()] for x in open('9_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
clusters = [[], [], []]
for p in l:
    if p[0] > 20:
        clusters[0].append(p)
    elif p[1] > 23:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
mn = []
ct1 = 0
ct2 = 0
ct3 = 0
for p1 in clusters[0]:
    if p1[-1][0] == 'Z' and p1[-1][2:] == 'I':
        ct1 += 1
    for p2 in clusters[0]:
        if p1 != p2 and p1[-1][0] == 'Z' and p1[-1][2:] == 'I' and p2[-1][0] == 'Z' and p2[-1][2:] == 'I':
            mn.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[1]:
    if p1[-1][0] == 'Z' and p1[-1][2:] == 'I':
        ct2 += 1
    for p2 in clusters[1]:
        if p1 != p2 and p1[-1][0] == 'Z' and p1[-1][2:] == 'I' and p2[-1][0] == 'Z' and p2[-1][2:] == 'I':
            mn.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[2]:
    if p1[-1][0] == 'Z' and p1[-1][2:] == 'I':
        ct3 += 1
    for p2 in clusters[2]:
        if p1 != p2 and p1[-1][0] == 'Z' and p1[-1][2:] == 'I' and p2[-1][0] == 'Z' and p2[-1][2:] == 'I':
            mn.append(math.dist(p1[:-1], p2[:-1]))
print(int(min(mn) * 10000), int(math.dist(centroids[0][:-1], centroids[2][:-1]) * 10000))
print(ct1, ct2, ct3)