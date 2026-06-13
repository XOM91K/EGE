import math
l = [x.replace(',','.').split() for x in open('12_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0]), float(l[x][1]), l[x][2]]
clusters = [[], [], []]
for p in l:
    if p[0] > 16:
        clusters[0].append(p)
    elif p[1] < 30:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
print(centroids)
ct = [0, 0, 0]
for p in clusters[0]:
    if p[2][0] == 'K' and p[2][2:] == 'III':
        ct[0] += 1
for p in clusters[1]:
    if p[2][0] == 'K' and p[2][2:] == 'III':
        ct[1] += 1
for p in clusters[2]:
    if p[2][0] == 'K' and p[2][2:] == 'III':
        ct[2] += 1
mx_rast = []
for p1 in clusters[0]:
    for p2 in clusters[0]:
        if p1[2][0] == 'G' and p1[2][2:] == 'V' and p2[2][0] == 'G' and p2[2][2:] == 'V':
            mx_rast.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[1]:
    for p2 in clusters[1]:
        if p1[2][0] == 'G' and p1[2][2:] == 'V' and p2[2][0] == 'G' and p2[2][2:] == 'V':
            mx_rast.append(math.dist(p1[:-1], p2[:-1]))z
for p1 in clusters[2]:
    for p2 in clusters[2]:
        if p1[2][0] == 'G' and p1[2][2:] == 'V' and p2[2][0] == 'G' and p2[2][2:] == 'V':
            mx_rast.append(math.dist(p1[:-1], p2[:-1]))
print(int(math.dist(centroids[0][:-1], centroids[1][:-1]) * 10000), int(max(mx_rast) * 10000))